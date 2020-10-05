import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import F, Q, Count, Case, When, OuterRef, Exists, BooleanField
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import filters, viewsets
from rest_framework_oauth.authentication import OAuth2Authentication

from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers
from openedx.core.djangoapps.theming.helpers import get_current_site
from openedx.features.redhouse_panel.api.v0.serializers import SiteSerializer, UserAccountSerializer
from openedx.features.redhouse_panel.api.permissions import CanAccessRedhousePanel
from student.models import CourseAccessRole
from student.roles import CourseStaffRole, CourseInstructorRole
from util.json_request import JsonResponse

logger = logging.getLogger(__name__)

User = get_user_model()


class UsersAccountStatsAPIView(APIView):
    authentication_classes = (
        JwtAuthentication,
        OAuth2Authentication,
        SessionAuthentication,
    )
    permission_classes = (IsAuthenticated, CanAccessRedhousePanel,)

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

        return JsonResponse(stats, status=status.HTTP_200_OK)


class SiteView(APIView):
    authentication_classes = (JwtAuthentication, OAuth2Authentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated, CanAccessRedhousePanel,)

    def get(self, request):
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
        site_configuration = configuration_helpers.get_current_site_configuration()
        data = {
            'name': site_configuration.get_value('school_name', settings.PLATFORM_NAME),
            'address': site_configuration.values.get('address') if site_configuration else '',
        }
        return JsonResponse(SiteSerializer(data).data)


class UserAccountView(viewsets.ModelViewSet):
    """
    Return the list of `Users` associated with the requested site

    Example:
        [
            {
                id: 2,
                is_superuser: true,
                username: "edx",
                email: "edx@example.com",
                is_staff: true,
                is_active: true,
                profile: {
                    name: "First Last",
                    year_of_birth: null
                },
                groups: [
                    {
                        name: "Redhouse Admin Panel Access"
                    }
                ]
            },
            ....
        ]
    """

    authentication_classes = (JwtAuthentication, OAuth2Authentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated, CanAccessRedhousePanel,)
    http_method_names = ['get', 'post', 'patch']
    filter_backends = (filters.SearchFilter,)
    search_fields = ['profile__name', 'username', 'email']
    serializer_class = UserAccountSerializer
    lookup_field = 'username'

    def get_queryset(self):
        site_organizations = configuration_helpers.get_current_site_orgs()

        return User.objects.select_related('profile').filter(
            Q(edly_profile__edly_sub_organizations__slug__in=site_organizations))
