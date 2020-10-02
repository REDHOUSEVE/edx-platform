"""
URLs for the Redhouse Panel v0 APIs.
"""
from django.conf.urls import include, url
from rest_framework import routers

from openedx.features.redhouse_panel.api.v0 import views

app_name = 'redhouse_panel_api.v0'

users_router = routers.DefaultRouter()
users_router.register(r'users', views.UserAccountView, base_name='users')


urlpatterns = [
    url(r'', include(users_router.urls)),
    url(r'^site/?$', views.SiteView.as_view(), name='site'),
    url(
        r'^account_stats/?$',
        views.UsersAccountStatsAPIView.as_view(),
        name='users_account_stats'
    ),
]
