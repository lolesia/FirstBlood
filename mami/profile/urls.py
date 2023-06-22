from rest_framework import routers
from .views import BreedViewSet, PetViewsSet

router = routers.DefaultRouter()

urlpatterns = []

router.register(r'', PetViewsSet)
router.register(r'breed', BreedViewSet)

urlpatterns += router.urls