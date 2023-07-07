from rest_framework import permissions


class PetPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_superuser:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        return False


class BreedPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        else:
            return request.user and request.user.is_superuser
