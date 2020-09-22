"""
URLs for the redhouse admin panel.
"""
from django.conf.urls import url, include

from openedx.features.redhouse_panel.views import render_redhouse_panel


app_name = 'redhouse_panel'

urlpatterns = [
    url(r'api/v0/', include('openedx.features.redhouse_panel.api.v0.urls')),

    url(r'', render_redhouse_panel, name='redhouse_panel'),
]
