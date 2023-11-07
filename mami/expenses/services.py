from .interfaces import ExpensesServiceInterface, ExpensesRepositoryInterface
from .dto import ExpensesCreateDTO, ExpensesDTO, TypeCreateDTO, TypeDTO


class ExpensesService(ExpensesServiceInterface):

    def __init__(self, expenses_repositories: ExpensesRepositoryInterface):
        self.expenses_repositories = expenses_repositories

    def create_expenses(self, create_expenses_dto: ExpensesCreateDTO) -> ExpensesDTO:
        return self.expenses_repositories.create_expenses(create_expenses_dto)

    def create_type(self, create_type_dto: TypeCreateDTO) -> TypeDTO:
        return self.expenses_repositories.create_type(create_type_dto)
