"""
URLs for the student support app.
"""
from django.conf.urls import url

from openedx.features.redhouse_features.views import email_support


app_name = 'redhouse_features'

urlpatterns = [
    url(r'^contact/$', email_support, name='email_support'),
]
