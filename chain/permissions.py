from rest_framework import permissions


class IsActive(permissions.BasePermission):
    message = 'Аккаунт не активирован. Обратитесь к администратору'

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False
