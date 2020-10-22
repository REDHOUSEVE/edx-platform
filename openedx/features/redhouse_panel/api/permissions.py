from rest_framework.permissions import BasePermission

from openedx.features.redhouse_panel.utils import has_panel_permission


class CanAccessRedhousePanel(BasePermission):

    def has_permission(self, request, view):
        return has_panel_permission(request.user)
