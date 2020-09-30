from rest_framework.permissions import BasePermission

from openedx.features.redhouse_panel.constants import REDHOUSE_PANEL_GROUP_NAME


class CanAccessRedhousePanel(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.user.groups.filter(name__in=[REDHOUSE_PANEL_GROUP_NAME]).exists()
