"""
URLs for the redhouse admin panel.
"""
from django.conf.urls import url, include

from openedx.features.admin_panel.views import render_admin_panel


app_name = 'redhouse_admin_panel'

urlpatterns = [
    url(r'api/v0/', include('openedx.features.admin_panel.api.v0.urls')),

    url(r'', render_admin_panel, name='admin_dashboard'),
]
