from .dto import UserDTO, UserRegistrationDTO
from .interfaces import UserServiceInterface, UserRepositoriesInterface


class UserService(UserServiceInterface):

    def __init__(self, user_repositories: UserRepositoriesInterface):
        self.user_repositories = user_repositories

    def user_registration(self, user_registration_dto: UserRegistrationDTO) -> UserDTO:
        return self.user_repositories.user_registration(user_registration_dto)
