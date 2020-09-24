from django.contrib.sites.models import Site
from django.shortcuts import get_object_or_404
from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_oauth.authentication import OAuth2Authentication

from openedx.core.djangoapps.site_configuration.models import SiteConfiguration
from openedx.core.lib.api.permissions import IsStaffOrOwner

from openedx.features.redhouse_panel.api.v0.serializers import SiteSerializer
from xmodule.modulestore.django import modulestore


class SiteView(APIView):
    authentication_classes = (JwtAuthentication, OAuth2Authentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated, IsStaffOrOwner,)

    def get(self, request, pk):
        """
        Return `Site` in the form of an object.
        Raises:
            NotFound: Raised if site with `pk` provided in `URL` does not exist.
        Example:
            `GET: /admin-panel/api/v0/site/1/`
            {
                "name": "Example Name",
                "address": "Silicon Valley"
            }
        """
        site = get_object_or_404(Site, pk=pk)
        site_configuration = SiteConfiguration.objects.filter(site=site).first()
        data = {
            'name': site.name,
            'address': site_configuration.values.get('address') if site_configuration else '',
        }
        return Response(SiteSerializer(data).data)


class CourseView(APIView):
    authentication_classes = (JwtAuthentication, OAuth2Authentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated, IsStaffOrOwner,)

    def get(self, request):
        """
        Return `courses` in the form of list
        Example:
            `GET: /admin-panel/api/v0/courses/`
            [
                course1,
                course2,
                course3
            ]
        """
        course_descriptors = modulestore().get_courses()
        courses = [course.location.course for course in course_descriptors]
        return Response(data=courses)
