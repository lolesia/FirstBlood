from .dto import ExpensesCreateDTO, ExpensesDTO, TypeCreateDTO, TypeDTO
from .interfaces import ExpensesServiceInterface


class ExpensesInteractor:

    def __init__(self, expenses_service: ExpensesServiceInterface):
        self.expenses_service = expenses_service

    def create_expenses(self, create_expenses_dto: ExpensesCreateDTO) -> ExpensesDTO:
        return self.expenses_service.create_expenses(create_expenses_dto)

    def create_type(self, create_type_dto: TypeCreateDTO) -> TypeDTO:
        return self.expenses_service.create_type(create_type_dto)