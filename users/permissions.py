from rest_framework.permissions import BasePermission


class IsModer(BasePermission):
    """Класс для разрешения доступа только модераторам"""

    def has_permission(self, request, view):
        """Права доступа для группы `moders`"""
        return request.user.groups.filter(
            name="moders"
        ).exists()  # Проверка принадлежности к группе


class IsOwner(BasePermission):
    """Класс для разрешения доступа только владельцам"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
