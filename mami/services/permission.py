from rest_framework.permissions import BasePermission, AllowAny, IsAdminUser


class ServicesPermission(BasePermission):
    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]

        print(f"Action: {self.action}")
        print(f"Permission classes: {permission_classes}")
        return [permission() for permission in permission_classes]