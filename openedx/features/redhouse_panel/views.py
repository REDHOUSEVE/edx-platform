"""
Sites admin dashboard views.
"""
from edxmako.shortcuts import render_to_response


def render_redhouse_panel(request):
    """
    View for admin panel dashboard.
    """
    return render_to_response('redhouse_panel/redhouse_panel.html')
