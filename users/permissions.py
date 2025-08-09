from rest_framework.permissions import BasePermission


class IsModer(BasePermission):
    """Класс для разрешения доступа только модераторам"""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()


class IsOwner(BasePermission):
    """Класс для разрешения доступа только владельцам"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
