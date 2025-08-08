from rest_framework.permissions import BasePermission


class IsModer(BasePermission):
    """Класс для разрешения доступа только модераторам"""

    def has_permission(self, request, view):
        request.user.groups.filter(name="Moderators").exists()

class IsOwner(BasePermission):
    """Класс для разрешения доступа только владельцам """

    def has_permission(self, request, view):
        request.user.groups.filter(name="Owners").exists()
