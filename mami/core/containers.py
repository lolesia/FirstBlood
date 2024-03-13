from dependency_injector import containers, providers

from expenses.interactors import ExpensesInteractor
from expenses.services import ExpensesService
from expenses.repositories import ExpensesRepository
from users.interactors import UserInteractor
from users.services import UserService
from users.repositories import UserRepositories
from pets.interactors import PetInteractor
from pets.services import PetService
from pets.repositories import PetRepositories


class RepositoryContainer(containers.DeclarativeContainer):
    expenses_repository = providers.Factory(ExpensesRepository)
    user_repositories = providers.Factory(UserRepositories)
    pet_repositories = providers.Factory(PetRepositories)


class ServicesContainer(containers.DeclarativeContainer):
    expenses_service = providers.Factory(ExpensesService, expenses_repository=RepositoryContainer.expenses_repository)
    user_service = providers.Factory(UserService, user_repositories=RepositoryContainer.user_repositories)
    pet_service = providers.Factory(PetService, pet_repositories=RepositoryContainer.pet_repositories)


class ProjectContainer(containers.DeclarativeContainer):
    expenses_interactor = providers.Factory(ExpensesInteractor, expenses_service=ServicesContainer.expenses_service)
    user_interactor = providers.Factory(UserInteractor, user_service=ServicesContainer.user_service)
    pet_interactor = providers.Factory(PetInteractor, pet_service=ServicesContainer.pet_service)