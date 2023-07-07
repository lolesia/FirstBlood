from rest_framework import viewsets
from .models import Breed, Pet
from .serializer import BreedSerializer, PetSerializer
from rest_framework.permissions import IsAdminUser
from .permission import PetPermission, BreedPermission


class BreedViewSet(viewsets.ModelViewSet):

    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = [BreedPermission]


class PetViewsSet(viewsets.ModelViewSet):

    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [PetPermission]