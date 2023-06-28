from rest_framework import routers
from .views import ServicesViewSet

router = routers.DefaultRouter()

urlpatterns = []
router.register(r'', ServicesViewSet)

urlpatterns += router.urls

