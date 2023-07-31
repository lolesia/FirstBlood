from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        record = view.get_object()
        return record.owner == request.user