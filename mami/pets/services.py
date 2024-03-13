from interfaces import PetServicesInterfaces, PetRepositoriesInterfaces
from mami.pets.dto import PetCreateDto, PetDto, BreedDto, BreedCreateDto


class PetService(PetServicesInterfaces):

    def __init__(self, pet_repositories: PetRepositoriesInterfaces):
        self.pet_repositories = pet_repositories

    def create_pet(self, pet_create_dto: PetCreateDto) -> PetDto:
        return self.pet_repositories.create_pet(pet_create_dto)

    def create_breed(self, breed_create_dto: BreedCreateDto) -> BreedDto:
        return self.pet_repositories.create_breed(breed_create_dto)
