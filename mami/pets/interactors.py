from .dto import PetDto, PetCreateDto, BreedDto, BreedCreateDto
from .interfaces import PetServicesInterfaces


class PetInteractor:

    def __init__(self, pet_service: PetServicesInterfaces):
        self.pet_service = pet_service

    def create_pet(self, pet_create_dto: PetCreateDto) -> PetDto:
        return self.pet_service.create_pet(pet_create_dto)

    def create_breed(self, breed_create_dto: BreedCreateDto) -> BreedDto:
        return self.pet_service.create_breed(breed_create_dto)
