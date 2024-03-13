from .interfaces import ExpensesServiceInterface, ExpensesRepositoryInterface
from .dto import ExpensesCreateDTO, ExpensesDTO, TypeCreateDTO, TypeDTO


class ExpensesService(ExpensesServiceInterface):

    def __init__(self, expenses_repository: ExpensesRepositoryInterface):
        self.expenses_repository = expenses_repository

    def get_expenses_by_id(self, expenses_id: int) -> ExpensesDTO:
        return self.expenses_repository.get_expenses_by_id(expenses_id)

    def get_expenses_by_groomer_id(self, groomer_id: int) -> ExpensesDTO:
        return self.expenses_repository.get_expenses_by_groomer_id(groomer_id)

    def create_expenses(self, create_expenses_dto: ExpensesCreateDTO) -> ExpensesDTO:
        return self.expenses_repository.create_expenses(create_expenses_dto)

    def get_type_by_id(self, type_id: int) -> TypeDTO:
        return self.expenses_repository.get_type_by_id(type_id)

    def create_type(self, create_type_dto: TypeCreateDTO) -> TypeDTO:
        return self.expenses_repository.create_type(create_type_dto)
