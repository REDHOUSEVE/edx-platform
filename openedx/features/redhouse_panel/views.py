"""
Sites admin dashboard views.
"""
from django.contrib.auth.decorators import login_required
from django.http import Http404
from edxmako.shortcuts import render_to_response

from openedx.features.redhouse_panel.waffle import waffle, ENABLE_REDHOUSE_PANEL


@login_required
def render_redhouse_panel(request):
    """
    View for admin panel dashboard.
    """
    if waffle().is_enabled(ENABLE_REDHOUSE_PANEL) and request.user.is_staff:
        return render_to_response('redhouse_panel/redhouse_panel.html')

    raise Http404
