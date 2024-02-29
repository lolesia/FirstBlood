from abc import ABCMeta, abstractmethod
from .dto import UserRegistrationDTO, UserDTO


class UserRepositoriesInterface(metaclass=ABCMeta):

    @abstractmethod
    def user_registration(self, user_registration_dto: UserRegistrationDTO) -> UserDTO:
        pass


class UserServiceInterface(metaclass=ABCMeta):

    @abstractmethod
    def user_registration(self, user_registration_dto: UserRegistrationDTO) -> UserDTO:
        pass
