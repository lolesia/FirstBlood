from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission, SAFE_METHODS, AllowAny, IsAuthenticated, IsAdminUser


class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return not request.user == AnonymousUser()

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.user


class ReviewsPermission(BasePermission):

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'destroy':
            permission_classes = (IsOwnerOrReadOnly, IsAdminUser, )
        elif self.action == 'update':
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]