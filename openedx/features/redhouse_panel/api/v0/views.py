from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.db.models import F, Q, Count, Case, When, OuterRef, Exists, BooleanField
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_oauth.authentication import OAuth2Authentication

from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
from openedx.core.djangoapps.site_configuration.models import SiteConfiguration
from openedx.core.djangoapps.theming.helpers import get_current_site
from openedx.core.lib.api.permissions import IsStaffOrOwner
from openedx.features.redhouse_panel.api.v0.serializers import SiteSerializer, UserSerializer
from student.models import CourseAccessRole
from student.roles import CourseStaffRole, CourseInstructorRole

User = get_user_model()


class UsersAccountStatsAPIView(APIView):
    authentication_classes = (
        JwtAuthentication,
        OAuth2Authentication,
        SessionAuthentication,
    )
    permission_classes = (IsAuthenticated, IsStaffOrOwner,)

    default_stats = {
        'instructor_count': 0,
        'student_count': 0
    }

    def get(self, request):
        site = get_current_site()

        site_users_query = Q(is_staff=True) | \
                           Q(edly_profile__edly_sub_organizations__lms_site=site) | \
                           Q(edly_profile__edly_sub_organizations__studio_site=site) | \
                           Q(edly_profile__edly_sub_organizations__preview_site=site)

        is_instructor_query = Exists(
            CourseAccessRole.objects.filter(
                user=OuterRef('id'),
                role__in=[CourseStaffRole.ROLE, CourseInstructorRole.ROLE]
            )
        )

        instructor_count_query = Count(
            Case(
                When(is_instructor=True, then=1)
            )
        )

        student_count_query = Count(
            Case(
                When(is_instructor=False, then=1)
            )
        )

        _stats = User.objects.filter(
            site_users_query
        ).annotate(
            is_instructor=is_instructor_query
        ).annotate(
            is_instructor=Case(
                When(is_staff=True, then=True),
                default=F('is_instructor'),
                output_field=BooleanField()
            )
        ).values(
            'is_instructor'
        ).annotate(
            # Conditional aggregation doesn't work with subquery annotations in django 1.11
            # https://code.djangoproject.com/ticket/30462
            # That's why used annotation to aggregate instructor/student account count
            instructor_count=instructor_count_query,
            student_count=student_count_query
        ).values(
            'instructor_count',
            'student_count'
        )

        stats = {}
        for stat in _stats or [self.default_stats]:
            for key, value in stat.items():
                if stats.get(key) is None:
                    stats[key] = 0
                stats[key] = stats[key] + stat[key]

        return Response(data=stats, status=status.HTTP_200_OK)


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


class UpdateUserActiveStatus(UpdateAPIView):
    """
    View to change user's active status
    Raises:
        NotFound: Raised if user with `pk` provided in `URL` does not exist.
    Example:
        `PUT/PATCH: /admin-panel/api/v0/users/1/update`
        body: {"is_active": false}
        :returns
            {
                "id": "1",
                "is_active": false
            }
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (SessionAuthentication, JwtAuthentication, OAuth2Authentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)

    def put(self, request, *args, **kwargs):
        request.data.pop('id', None)
        return self.partial_update(request, *args, **kwargs)
