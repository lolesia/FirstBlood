from .dto import UserDTO, UserRegistrationDTO
from .interfaces import UserServiceInterface


class UserInteractor:

    def __init__(self, user_service: UserServiceInterface):
        self.user_service = user_service

    def user_registration(self, user_registration_dto: UserRegistrationDTO) -> UserDTO:
        return self.user_service.user_registration(user_registration_dto)
