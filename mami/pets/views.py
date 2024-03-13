from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from core.containers import ProjectContainer

from .dto import PetCreateDto, PetDto, BreedDto, BreedCreateDto
from .serializer import PetDTOSerializer, PetCreateDTOSerializer, BreedCreateDTOSerializer, BreedDTOSerializer


class BreedAPIView(APIView):

    def __init__(self):
        super().__init__()
        self.pet_interactor = ProjectContainer.pet_interactor()

    def post(self, request):

        create_breed = BreedCreateDTOSerializer(data=request.data)
        if not create_breed.is_valid():
            return Response(create_breed.errors, status=status.HTTP_400_BAD_REQUEST)

        create_breed_dto = BreedCreateDto(**create_breed.validated_data)
        create_breed = self.pet_interactor.create_breed(create_breed_dto)
        breed_serializer = BreedDTOSerializer(create_breed)
        return Response(
            data=breed_serializer.data,
            status=status.HTTP_200_OK,
        )


class PetAPIView(APIView):
    def __init__(self):
        super().__init__()
        self.pet_interactor = ProjectContainer.pet_interactor()

    def post(self, request):

        create_pet = PetCreateDTOSerializer(data=request.data)
        if not create_pet.is_valid():
            return Response(create_pet.errors, status=status.HTTP_400_BAD_REQUEST)

        create_pet_dto = PetCreateDto(**create_pet.validated_data)
        create_pet = self.pet_interactor.create_pet(create_pet_dto)
        pet_serializer = BreedDTOSerializer(create_pet)
        return Response(
            data=pet_serializer.data,
            status=status.HTTP_200_OK
        )

    def get(self, request, id):
        try:
            pet = self.pet_interactor.get_pet_by_id(pet_id=id)
        except NotFound:
            return Response({"detail": f"Pet with {id} not found"}, status=status.HTTP_404_NOT_FOUND)
        pet_serializer = PetDTOSerializer(pet)
        return Response(
            data=pet_serializer.data,
            status=status.HTTP_200_OK
        )