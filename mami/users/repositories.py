from .dto import UserDTO, UserRegistrationDTO
from .interfaces import UserRepositoriesInterface
from .serializer import UserRegistrationSerializer

from profiles.models import Owner, Groomer
from .models import User

from annoying.functions import get_object_or_None
from typing import Dict, Type
from django.db import models, IntegrityError, DatabaseError
from core.exceptions import InstanceAlreadyExistsError, InstanceCreationError


class UserRepositories(UserRepositoriesInterface):

    PROFILE_TYPE: Dict[str, Type[models.Model]]

    def user_registration(self, user_registration_dto: UserRegistrationDTO) -> UserDTO:

        try:
            user = User.objects.create_user(email=user_registration_dto.email, password=user_registration_dto.password)

        except IntegrityError:
            raise InstanceAlreadyExistsError(f"A user with email {user_registration_dto.email} already exists!")

        except DatabaseError as e:
            raise InstanceCreationError(f"An error occurred while creating the user. Details: {str(e)}")

        user.is_active = False
        user.save()

        profile_class = self.PROFILE_TYPE[user_registration_dto.profile_type]

        profile_class.objects.create(user=user, first_name=user_registration_dto.first_name)

        return self._user_to_dto(user)

    @staticmethod
    def _user_to_dto(user: User) -> UserDTO:
        return UserDTO(
            id=user.pk,
            email=user.email,
            phone=user.phone,
            is_active=user.is_active
        )



