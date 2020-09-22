"""
URLs for the Admin panel v0 APIs.
"""

from django.conf.urls import url

from .users_account_stats import UsersAccountStatsAPIView

app_name = 'redhouse_panel_api.v0'


urlpatterns = [
    url(
        r'^sites/(?P<pk>\d+)/account_stats/?$',
        UsersAccountStatsAPIView.as_view(),
        name='users_account_stats'
    ),
]
