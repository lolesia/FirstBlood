from rest_framework import routers
from .views import VisitsViewSet

router = routers.DefaultRouter()

urlpatterns = []

router.register(r'', VisitsViewSet)

urlpatterns += router.urls