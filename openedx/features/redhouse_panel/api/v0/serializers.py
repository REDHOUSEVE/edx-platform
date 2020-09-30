from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

from openedx.features.edly.utils import create_user_link_with_edly_sub_organization
from openedx.features.redhouse_panel.constants import REDHOUSE_PANEL_GROUP_NAME
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
    can_access_panel = serializers.SerializerMethodField('has_panel_permission')

    class Meta:
        model = User
        read_only_fields = ('id',)
        fields = ('username', 'email', 'is_active', 'profile', 'can_access_panel')

    @staticmethod
    def has_panel_permission(obj):
        if obj.groups.filter(name__in=[REDHOUSE_PANEL_GROUP_NAME]).exists():
            return True
        return False

    def create(self, validated_data):
        # create user
        profile_data = validated_data.pop('profile')
        can_access_panel = self.initial_data.get('can_access_panel', None)

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

        #TODO
        # send_password_set_email_to_user()
        return user

    def update(self, user, validated_data):
        profile_data = validated_data.pop('profile', None)
        can_access_panel = self.initial_data.get('can_access_panel', None)

        # updating user data
        user.is_superuser = validated_data.get('is_superuser', user.is_superuser)
        user.username = validated_data.get('username', user.username)
        user.email = validated_data.get('email', user.email)
        user.is_staff = validated_data.get('is_staff', user.is_staff)
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

        return user
