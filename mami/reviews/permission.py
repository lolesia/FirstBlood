from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS, AllowAny, IsAuthenticated, IsAdminUser


class ReviewsPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or request.method in ['GET', 'POST']:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method in ['PUT', 'PATCH', 'DELETE']:
            return obj.author == request.user or request.user.is_superuser
        return False