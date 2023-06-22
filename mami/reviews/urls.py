from rest_framework import routers
from .views import ReviewsViewSet

router = routers.DefaultRouter()

urlpatterns = []

router.register(r'', ReviewsViewSet)

urlpatterns += router.urls

