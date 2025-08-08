from rest_framework.permissions import BasePermission


class ModeratorRights(BasePermission):
    """Класс для разрешения доступа только модераторам"""

    def has_permission(self, request, view):
        request.user.groups.filter(name="Moderators").exists()
