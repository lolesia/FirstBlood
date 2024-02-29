from dependency_injector import containers, providers

from expenses.interactors import ExpensesInteractor
from expenses.services import ExpensesService
from expenses.repositories import ExpensesRepository
from users.interactors import UserInteractor
from users.services import UserService
from users.repositories import UserRepositories


class RepositoryContainer(containers.DeclarativeContainer):
    expenses_repository = providers.Factory(ExpensesRepository)
    user_repositories = providers.Factory(UserRepositories)


class ServicesContainer(containers.DeclarativeContainer):
    expenses_services = providers.Factory(ExpensesService, expenses_repository=RepositoryContainer.expenses_repository)
    user_services = providers.Factory(UserService, user_repositories=RepositoryContainer.user_repositories)


class ProjectContainer(containers.DeclarativeContainer):
    expenses_interactor = providers.Factory(ExpensesInteractor, expenses_services=ServicesContainer.expenses_services)
    user_interactor = providers.Factory(UserInteractor, user_services=ServicesContainer.user_services)
