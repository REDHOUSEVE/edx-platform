from django.test import TestCase
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

    def test_with_staff_user(self):
        # is_staff = True

        self.client.login(
            username=self.staff.username,
            password=self.PASSWORD
        )

        url = reverse(
            'redhouse_features:redhouse_panel:redhouse_panel_api.v0:users_account_stats',
            kwargs={'pk': self.staff.edly_profile.edly_sub_organizations.first().lms_site.id}
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['instructor_count'], 1)
        self.assertEqual(response.data['student_count'], 1)

    def test_with_non_staff_user(self):
        # is_staff = False

        self.client.login(
            username=self.student.username,
            password=self.PASSWORD
        )

        url = reverse(
            'redhouse_features:redhouse_panel:redhouse_panel_api.v0:users_account_stats',
            kwargs={'pk': self.student.edly_profile.edly_sub_organizations.first().lms_site.id}
        )

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
