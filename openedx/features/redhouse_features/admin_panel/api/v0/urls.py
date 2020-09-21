"""
URLs for the Admin panel v0 APIs.
"""
from django.conf.urls import url

from . import views

app_name = 'redhouse_admin.api.v0'

urlpatterns = [
    url(r'^site/(?P<pk>\d+)/$', views.SiteView.as_view(), name='site'),
]
