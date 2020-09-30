import json

from django.urls import reverse
from django.test import TestCase
from rest_framework import status

from openedx.features.edly.tests.factories import EdlyUserFactory


class UsersActiveStatusAPIViewTest(TestCase):
    PASSWORD = 'edx'

    USER_CREDENTIALS = {
        'staff': {
            'username': 'edx',
            'email': 'edx@example.com',
            'password': PASSWORD,
            'is_staff': True,
        },
        'active_user': {
            'username': 'user1',
            'email': 'user1@example.com',
            'password': PASSWORD,
            'is_active': True,
        }
    }

    def setUp(self):
        self.staff = EdlyUserFactory(**self.USER_CREDENTIALS['staff'])
        self.active = EdlyUserFactory(**self.USER_CREDENTIALS['active_user'])

        self.url = reverse(
            'redhouse_panel:redhouse_panel_api.v0:update_user_active_status',
            kwargs={'pk': self.active.id}
        )

    def test_with_staff_user(self):
        self.client.login(username=self.staff.username, password=self.PASSWORD)
        response = self.client.patch(self.url, json.dumps({'is_active': False}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.active.id)
        self.assertEqual(response.data['is_active'], False)

    def test_for_unauthenticated_user(self):
        response = self.client.patch(self.url, json.dumps({'is_active': False}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')
