"""
Sites admin dashboard views.
"""
from edxmako.shortcuts import render_to_response


def render_admin_panel(request):
    """
    View for admin panel dashboard.
    """
    return render_to_response('admin_panel/admin_panel.html')
