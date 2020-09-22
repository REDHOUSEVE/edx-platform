from django.conf import settings
from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse
from rest_framework import status

from openedx.core.djangoapps.site_configuration.tests.factories import SiteConfigurationFactory, SiteFactory
from openedx.features.edly import cookies
from openedx.features.edly.tests.factories import EdlySubOrganizationFactory, EdlyUserFactory
from student.tests.factories import UserFactory


class SiteViewTests(TestCase):
    USERNAME = "edx"
    EMAIL = "edx@example.com"
    PASSWORD = "edx"

    def setUp(self):
        self.staff = UserFactory.create(
            username=self.USERNAME,
            email=self.EMAIL,
            password=self.PASSWORD,
            is_staff=True
        )
        self.client.login(username=self.USERNAME, password=self.PASSWORD)
        self.site_name = 'fake.name'
        self.site_address = 'fake.address'

    def test_return_site_successfully(self):
        site = SiteFactory(name=self.site_name)
        site_configuration = SiteConfigurationFactory(values={'address': self.site_address}, site=site)

        url = reverse('redhouse_panel:redhouse_panel_api.v0:site', kwargs={'pk': site.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.site_name)
        self.assertEqual(response.data['address'], self.site_address)

    def test_for_unauthenticated_user_return_error(self):
        site = SiteFactory(name=self.site_name)
        site_configuration = SiteConfigurationFactory(values={'address': self.site_address}, site=site)
        url = reverse('redhouse_panel:redhouse_panel_api.v0:site', kwargs={'pk': site.id})

        self.client.logout()

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')

    def test_non_existent_site_return_error(self):
        url = reverse('redhouse_panel:redhouse_panel_api.v0:site', kwargs={'pk': 2})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'], 'Not found.')

    def test_non_existent_site_configuration_return_empty_address(self):
        site = SiteFactory(name=self.site_name)

        url = reverse('redhouse_panel:redhouse_panel_api.v0:site', kwargs={'pk': site.id})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], site.name)
        self.assertEqual(response.data['address'], '')
    
    def test_for_non_staff_user_return_error(self):
        password = 'fake.password'
        user = EdlyUserFactory(password=password)
        site = SiteFactory(name=self.site_name)
        site_config = SiteConfigurationFactory(values={'address': self.site_address}, site=site)
        EdlySubOrganizationFactory(lms_site=site)
        request = RequestFactory()
        request.user = user
        request.site = site

        self.client.login(username=user.username, password=password)
        self.client.cookies.load(
            {
                settings.EDLY_USER_INFO_COOKIE_NAME: cookies._get_edly_user_info_cookie_string(request)
            }
        )
        url = reverse('redhouse_panel:redhouse_panel_api.v0:site', kwargs={'pk': site.id})
        response = self.client.get(url, SERVER_NAME=site.domain)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'], 'You do not have permission to perform this action.')
