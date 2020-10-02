from django.contrib.auth import get_user_model
from rest_framework import serializers

from openedx.features.edly.utils import (
    create_user_link_with_edly_sub_organization,
    get_edx_org_from_cookie
)
from openedx.features.redhouse_panel.utils import (
    set_global_course_creator_status,
    has_panel_permission,
    has_course_creator_permissions,
    set_panel_access
)
from student.models import UserProfile

User = get_user_model()


class SiteSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('name', 'year_of_birth')


class UserAccountSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    can_access_panel = serializers.SerializerMethodField('has_panel_access')
    is_instructor = serializers.SerializerMethodField('can_create_courses')

    class Meta:
        model = User
        read_only_fields = ('id',)
        fields = ('username', 'email', 'is_active', 'profile', 'can_access_panel', 'is_instructor')

    @staticmethod
    def has_panel_access(obj):
        return has_panel_permission(obj)

    def can_create_courses(self, obj):
        request = self.context['request']
        return has_course_creator_permissions(request, obj)

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        can_access_panel = self.initial_data.get('can_access_panel', None)
        is_instructor = self.initial_data.get('is_instructor', None)

        user = User.objects.create(**validated_data)

        UserProfile.objects.create(user=user, **profile_data)

        request = self.context['request']
        create_user_link_with_edly_sub_organization(request, user)

        if can_access_panel:
            set_panel_access(user, can_access_panel)

        if is_instructor:
            # We are only setting the user as GlobalCourseInstructor, which means the user
            # will see all of the organization's courses. We can make the user only CourseCreator,
            # but it is not clear for now. If requirements get change in the future, we need to add some code here.
            set_global_course_creator_status(request, user, is_instructor)

        #TODO
        # send_password_set_email_to_user()
        return user

    def update(self, user, validated_data):
        profile_data = validated_data.pop('profile', None)
        request = self.context['request']

        user.email = validated_data.get('email', user.email)
        user.is_active = validated_data.get('is_active', user.is_active)
        user.save(update_fields=['is_active', 'email'])

        if profile_data:
            UserProfile.objects.update_or_create(
                user=user,
                defaults={
                    'name': profile_data.get('name'),
                    'year_of_birth': profile_data.get('year_of_birth')
                }
            )

        if 'can_access_panel' in self.initial_data.keys():
            can_access_panel = self.initial_data.get('can_access_panel')
            set_panel_access(user, can_access_panel)

        if 'is_instructor' in self.initial_data.keys():
            # We are only setting the user as GlobalCourseInstructor, which means the user
            # will see all of the organization's courses. We can make the user only CourseCreator,
            # but it is not clear for now. If requirements get change in the future, we need to add some code here.
            is_instructor = self.initial_data.get('is_instructor')
            set_global_course_creator_status(request, user, is_instructor)

        return user

    def is_valid(self, raise_exception=False):
        try:
            super(UserAccountSerializer, self).is_valid(raise_exception)
        except serializers.ValidationError:
            pass

        errors = self.errors.copy()
        extra_fields = ['is_instructor', 'can_access_panel']
        for field in extra_fields:
            if field in self.initial_data.keys():
                if type(self.initial_data[field]) != bool:
                    errors[field] = ['"{}" is not a valid boolean.'.format(self.initial_data.get(field))]
        if errors:
            raise serializers.ValidationError(errors)
