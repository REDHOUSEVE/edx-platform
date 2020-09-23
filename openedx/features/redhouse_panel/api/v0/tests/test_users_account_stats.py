from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from rest_framework import status

from openedx.features.edly.tests.factories import (
    EdlyUserFactory,
    EdlyUserProfileFactory,
    EdlySubOrganizationFactory,
)


class UsersAccountStatsAPIViewTest(TestCase):
    PASSWORD = 'edx'

    USER_CREDENTIALS = {
        'staff': {
            'username': 'edx',
            'email': 'edx@example.com',
            'password': PASSWORD,
            'is_staff': True,
        },
        'student': {
            'username': 'test',
            'email': 'test@example.com',
            'password': PASSWORD,
            'is_staff': False,
        }
    }

    def setUp(self):
        self.staff = EdlyUserFactory(
            **self.USER_CREDENTIALS['staff']
        )
        self.edly_sub_organizations = [EdlySubOrganizationFactory()]

        edly_user_profile = EdlyUserProfileFactory(user=self.staff)
        edly_user_profile.edly_sub_organizations.add(*self.edly_sub_organizations)

        self.student = EdlyUserFactory(
            **self.USER_CREDENTIALS['student']
        )
        edly_user_profile = EdlyUserProfileFactory(user=self.student)
        edly_user_profile.edly_sub_organizations.add(*self.edly_sub_organizations)

        self.site = self.staff.edly_profile.edly_sub_organizations.first().lms_site

        self.client = Client(site=self.site, SERVER_NAME=self.site.domain)

    def test_with_global_staff_user(self):
        self.client.login(
            username=self.staff.username,
            password=self.PASSWORD
        )

        url = reverse('redhouse_panel:redhouse_panel_api.v0:users_account_stats')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['instructor_count'], 1)
        self.assertEqual(response.data['student_count'], 1)

    def test_for_unauthenticated_user_return_error(self):
        url = reverse('redhouse_panel:redhouse_panel_api.v0:users_account_stats')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')
