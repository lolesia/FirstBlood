from .interfaces import ExpensesRepositoryInterface
from .models import Expenses, Type
from .dto import ExpensesCreateDTO, ExpensesDTO, TypeCreateDTO, TypeDTO


class ExpensesRepository(ExpensesRepositoryInterface):

    def create_expenses(self, create_expenses_dto: ExpensesCreateDTO) -> ExpensesDTO:

        expenses = Expenses.objects.create(
            type=create_expenses_dto.type,
            name=create_expenses_dto.name,
            cost=create_expenses_dto.cost,
            date=create_expenses_dto.date,
            comment=create_expenses_dto.comment,
        )

        return self._expenses_to_dto(expenses)

    @staticmethod
    def _expenses_to_dto(expenses: Expenses) -> ExpensesDTO:

        return ExpensesDTO(
            id=expenses.pk,
            type=expenses.type,
            name=expenses.name,
            cost=expenses.cost,
            date=expenses.date,
            comment=expenses.comment
        )

    def create_type(self, create_type_dto: TypeCreateDTO) -> TypeDTO:

        types = Type.objects.create(
            type=create_type_dto.type
        )

        return self._type_to_dto(types)

    @staticmethod
    def _type_to_dto(types: Type) -> TypeDTO:
        return TypeDTO(
            id=types.pk,
            type=types.type
        )
