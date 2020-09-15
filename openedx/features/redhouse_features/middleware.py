"""
Middleware for the redhouse app
"""

from django.http import Http404
from django.urls import resolve

from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers


class BlockingUrlMiddleware(object):
    """
    Django middleware object to return 404 on certain url names
    """

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        runs before any view and will block the url name mentioned in BLOCKED_URL_NAMES
        as a list in site configurations
        """

        blocked_url_names = configuration_helpers.get_value('BLOCKED_URL_NAMES')
        if blocked_url_names and resolve(request.path).url_name in blocked_url_names:
            raise Http404
