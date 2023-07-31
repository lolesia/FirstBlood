from rest_framework import viewsets, permissions
from .serializer import UserSerializer
from .models import User
from .permission import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ['update', 'partial_update']:
            self.permission_classes = [IsOwnerOrReadOnly]
        elif self.action == 'destroy':
            self.permission_classes = [permissions.IsAdminUser]

        return super().get_permissions()



