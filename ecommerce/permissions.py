from rest_framework import permissions


class IsVender(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role.role.lower() == 'vendor'

class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role.role.lower() == 'user'

