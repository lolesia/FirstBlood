from abc import ABCMeta, abstractmethod
from .dto import PetCreateDto, PetDto, BreedDto, BreedCreateDto


class PetRepositoriesInterfaces(metaclass=ABCMeta):

    @abstractmethod
    def create_pet(self, pet_create_dto: PetCreateDto) -> PetDto:
        pass

    @abstractmethod
    def create_breed(self, breed_create_dto: BreedCreateDto) -> BreedDto:
        pass


class PetServicesInterfaces(metaclass=ABCMeta):

    @abstractmethod
    def create_pet(self, pet_create_dto: PetCreateDto) -> PetDto:
        pass

    @abstractmethod
    def create_breed(self, breed_create_dto: BreedCreateDto) -> BreedDto:
        pass

