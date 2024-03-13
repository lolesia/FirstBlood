from .interfaces import PetRepositoriesInterfaces
from .models import Pet, Breed
from .dto import PetCreateDto, PetDto, BreedCreateDto, BreedDto

from annoying.functions import get_object_or_None


class PetRepositories(PetRepositoriesInterfaces):

    def get_pet_by_id(self, pet_id: int) -> PetDto:

        pet = get_object_or_None(Pet, pet_id)

        return self._pet_to_dto(pet)

    def create_pet(self, pet_create_dto: PetCreateDto) -> PetDto:

        pet = Pet.objects.create(
            pet_name=pet_create_dto.pet_name,
            breed=pet_create_dto.breed,
            weight=pet_create_dto.weight,
            photo=pet_create_dto.photo,
            description=pet_create_dto.description

        )
        return self._pet_to_dto(pet)

    @staticmethod
    def _pet_to_dto(pet: Pet) -> PetDto:
        return PetDto(
            id=pet.pk,
            owner='{} {}'.format(pet.owner.first_name, pet.owner.last_name),
            owner_id=pet.owner.user.id,
            pet_name=pet.pet_name,
            breed=pet.breed,
            weight=pet.weight,
            photo=pet.photo,
            description=pet.description,
        )

    def create_breed(self, breed_create_dto: BreedCreateDto) -> BreedDto:

        breed = Breed.objects.create(
            breed=breed_create_dto.breed
        )
        return self._breed_to_dto(breed)

    @staticmethod
    def _breed_to_dto(breed: Breed) -> BreedDto:
        return BreedDto(
            id=breed.pk,
            breed=breed.breed,
        )
