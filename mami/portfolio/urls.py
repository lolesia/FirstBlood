from rest_framework import routers
from .views import PortfolioViewSet

router = routers.DefaultRouter()

urlpatterns = []

router.register(r'', PortfolioViewSet)


urlpatterns += router.urls
