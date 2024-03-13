from dataclasses import dataclass


@dataclass(frozen=True)
class BreedDto:

    id: int
    breed: str


@dataclass(frozen=True)
class BreedCreateDto:

    breed: str


@dataclass(frozen=True)
class PetDto:

    id: int
    owner: str
    owner_id: int
    pet_name: str
    breed: str
    weight: float
    photo: str | None
    description: str


@dataclass(frozen=True)
class PetCreateDto:

    pet_name: str
    breed: str
    weight: float
    photo: str | None
    description: str


