from .dto import ExpensesCreateDTO, ExpensesDTO, TypeCreateDTO, TypeDTO
from .interfaces import ExpensesServiceInterface


class ExpensesInteractor:

    def __init__(self, expenses_service: ExpensesServiceInterface):
        self.expenses_service = expenses_service

    def get_expenses_by_groomer_id(self, groomer_id: int) -> ExpensesDTO:
        return self.expenses_service.get_expenses_by_groomer_id(groomer_id)

    def get_expenses_by_id(self, groomer_id: int) -> ExpensesDTO:
        return self.expenses_service.get_expenses_by_id(groomer_id)

    def create_expenses(self, create_expenses_dto: ExpensesCreateDTO) -> ExpensesDTO:
        return self.expenses_service.create_expenses(create_expenses_dto)

    def get_type_by_id(self, type_id: int) -> TypeDTO:
        return self.expenses_service.get_type_by_id(type_id)

    def create_type(self, create_type_dto: TypeCreateDTO) -> TypeDTO:
        return self.expenses_service.create_type(create_type_dto)
