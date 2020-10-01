from datetime import datetime
from django.conf import settings

from openedx.features.edly.utils import (
    get_edx_org_from_cookie,
    update_course_creator_status,
)

from student.roles import (
    CourseInstructorRole,
    CourseStaffRole,
    GlobalCourseCreatorRole,
    GlobalStaff,
    UserBasedRole,
)


def set_global_course_creator_status(request, user, set_global_creator):
    """
    Updates global course creator status of a user.
    """
    from course_creators.models import CourseCreator
    from course_creators.views import update_course_creator_group

    request_user = request.user

    course_creator, __ = CourseCreator.objects.get_or_create(user=user)
    course_creator.state = CourseCreator.GRANTED if set_global_creator else CourseCreator.UNREQUESTED
    course_creator.note = 'Global course creator user was updated by panel admin {} on {}'.format(
        request_user.email, datetime.now())
    course_creator.admin = request_user
    course_creator.save()
    edly_user_info_cookie = request.COOKIES.get(settings.EDLY_USER_INFO_COOKIE_NAME, None)
    edx_org = get_edx_org_from_cookie(edly_user_info_cookie)
    update_course_creator_group(request_user, user, set_global_creator)
    if set_global_creator:
        GlobalCourseCreatorRole(edx_org).add_users(user)
    else:
        GlobalCourseCreatorRole(edx_org).remove_users(user)
        instructor_courses = UserBasedRole(user, CourseInstructorRole.ROLE).courses_with_role()
        staff_courses = UserBasedRole(user, CourseStaffRole.ROLE).courses_with_role()
        instructor_courses_keys = [course.course_id for course in instructor_courses]
        staff_courses_keys = [course.course_id for course in staff_courses]
        UserBasedRole(user, CourseInstructorRole.ROLE).remove_courses(*instructor_courses_keys)
        UserBasedRole(user, CourseStaffRole.ROLE).remove_courses(*staff_courses_keys)
