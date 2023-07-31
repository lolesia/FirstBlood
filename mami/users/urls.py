from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()

urlpatterns = []

router.register(r'', UserViewSet)

urlpatterns += router.urls

