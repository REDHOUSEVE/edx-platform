from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

from openedx.features.edly.utils import (
    create_user_link_with_edly_sub_organization,
    get_edx_org_from_cookie
)
from openedx.features.redhouse_panel.constants import REDHOUSE_PANEL_GROUP_NAME
from openedx.features.redhouse_panel.utils import set_global_course_creator_status
from student import auth
from student.models import UserProfile
from student.roles import CourseCreatorRole, GlobalCourseCreatorRole

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
    can_access_panel = serializers.SerializerMethodField('has_panel_permission')
    is_instructor = serializers.SerializerMethodField('can_create_courses')

    class Meta:
        model = User
        read_only_fields = ('id',)
        fields = ('username', 'email', 'is_active', 'profile', 'can_access_panel', 'is_instructor')

    def has_panel_permission(self, obj):
        if obj.groups.filter(name__in=[REDHOUSE_PANEL_GROUP_NAME]).exists():
            return True
        return False

    def can_create_courses(self, obj):
        request = self.context['request']
        edly_user_info_cookie = request.COOKIES.get(settings.EDLY_USER_INFO_COOKIE_NAME, None) if request else None
        edx_org = get_edx_org_from_cookie(edly_user_info_cookie)

        if auth.user_has_role(obj, GlobalCourseCreatorRole(edx_org)):
            return True
        return False

    def create(self, validated_data):
        # create user
        profile_data = validated_data.pop('profile')
        can_access_panel = self.initial_data.get('can_access_panel', None)
        is_instructor = self.initial_data.get('is_instructor', None)

        user = User.objects.create(**validated_data)

        # create profile
        UserProfile.objects.create(
            user=user,
            name=profile_data.get('name', None),
            year_of_birth=profile_data.get('year_of_birth', None)
        )

        # create EdlyUserProfile
        request = self.context['request']
        create_user_link_with_edly_sub_organization(request, user)

        if can_access_panel:
            panel_group, _ = Group.objects.get_or_create(name=REDHOUSE_PANEL_GROUP_NAME)
            user.groups.add(panel_group)

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
        can_access_panel = self.initial_data.get('can_access_panel', None)
        request = self.context['request']

        # updating user data
        user.email = validated_data.get('email', user.email)
        user.is_active = validated_data.get('is_active', user.is_active)
        user.save()

        if profile_data:
            # updating profile data
            UserProfile.objects.update_or_create(
                user=user,
                defaults={
                    'name': profile_data.get('name', None),
                    'year_of_birth': profile_data.get('year_of_birth', None)
                }
            )

        if can_access_panel and not user.groups.filter(name__in=[REDHOUSE_PANEL_GROUP_NAME]).exists():
            panel_group, _ = Group.objects.get_or_create(name=REDHOUSE_PANEL_GROUP_NAME)
            user.groups.add(panel_group)

        if 'is_instructor' in self.initial_data.keys():
            # We are only setting the user as GlobalCourseInstructor, which means the user
            # will see all of the organization's courses. We can make the user only CourseCreator,
            # but it is not clear for now. If requirements get change in the future, we need to add some code here.
            is_instructor = self.initial_data.get('is_instructor')
            set_global_course_creator_status(request, user, is_instructor)

        return user
