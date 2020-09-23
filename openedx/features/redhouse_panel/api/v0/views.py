from django.contrib.auth import get_user_model
from django.db.models import F, Q, Count, Case, When, OuterRef, Exists, BooleanField
from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
from openedx.core.djangoapps.theming.helpers import get_current_site
from openedx.core.lib.api.permissions import IsStaffOrOwner
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_oauth.authentication import OAuth2Authentication
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

        _stats = get_user_model().objects.filter(
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
