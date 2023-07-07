from rest_framework import permissions


class PortfolioPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        else:
            return request.user and request.user.is_superuser