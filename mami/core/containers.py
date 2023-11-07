from dependency_injector import containers, providers

from expenses.interactors import ExpensesInteractor
from expenses.services import ExpensesService
from expenses.repositories import ExpensesRepository


class RepositoryContainer(containers.DeclarativeContainer):
    expenses_repository = providers.Factory(ExpensesRepository)


class ServicesContainer(containers.DeclarativeContainer):
    expenses_services = providers.Factory(ExpensesService, expenses_repository=RepositoryContainer.expenses_repository)


class ProjectContainer(containers.DeclarativeContainer):
    expenses_interactor = providers.Factory(ExpensesInteractor, expenses_services=ServicesContainer.expenses_services)
