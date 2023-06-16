from rest_framework import routers
from .views import ExpensesViewSet, TypeViewSet

router = routers.DefaultRouter()

urlpatterns = []

router.register(r'', ExpensesViewSet)
router.register(r'type', TypeViewSet)

urlpatterns += router.urls
