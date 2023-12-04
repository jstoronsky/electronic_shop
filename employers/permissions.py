from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    message = 'У пользователя нет прав доступа'

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False
