from rest_framework import viewsets
from .models import Breed, Pet
from .serializer import BreedSerializer, PetSerializer
from rest_framework.permissions import IsAdminUser
from .permission import IsOwnerOrRedOnly


class BreedViewSet(viewsets.ModelViewSet):

    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class PetViewsSet(viewsets.ModelViewSet):

    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsOwnerOrRedOnly, IsAdminUser]