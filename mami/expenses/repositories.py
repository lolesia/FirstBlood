from django.db.models import QuerySet
from django.core.exceptions import ObjectDoesNotExist

from .interfaces import ExpensesRepositoryInterface
from .models import Expenses, Type
from .dto import ExpensesCreateDTO, ExpensesDTO, TypeCreateDTO, TypeDTO
from annoying.functions import get_object_or_None
from django.shortcuts import get_list_or_404


class ExpensesRepository(ExpensesRepositoryInterface):

    def get_expenses_by_id(self, expenses_id: int) -> ExpensesDTO:

        expenses = get_object_or_None(Expenses, id=expenses_id)
        if not expenses:
            raise ObjectDoesNotExist(f"Expenses with id {expenses_id} not found")

        return self._expense_to_dto(expenses)

    def get_expenses_by_groomer_id(self, groomer_id: int) -> list[ExpensesDTO]:

        expenses = Expenses.objects.filter(groomer__user__id=groomer_id)
        if not expenses:
            raise ObjectDoesNotExist(f"This groomer {groomer_id} not has no expenses yet")

        return self._expenses_to_dto(expenses)

    def create_expenses(self, create_expenses_dto: ExpensesCreateDTO) -> ExpensesDTO:

        expenses = Expenses.objects.create(
            type_id=create_expenses_dto.type,
            name=create_expenses_dto.name,
            cost=create_expenses_dto.cost,
            date=create_expenses_dto.date,
            comment=create_expenses_dto.comment,
        )

        return self._expense_to_dto(expenses)

    @staticmethod
    def _expense_to_dto(expenses: Expenses) -> ExpensesDTO:

        return ExpensesDTO(
            id=expenses.pk,
            type=expenses.type,
            name=expenses.name,
            cost=expenses.cost,
            date=expenses.date,
            comment=expenses.comment
        )

    @staticmethod
    def _expenses_to_dto(expenses: QuerySet[Expenses]) -> list[ExpensesDTO]:
        expenses_dto = [ExpensesRepository._expense_to_dto(expense) for expense in expenses]
        return expenses_dto

    def get_type_by_id(self, type_id: int) -> TypeDTO:

        type_by_id = get_object_or_None(Type, id=type_id)
        if not type_by_id:
            raise ObjectDoesNotExist(f"Type with id {type_id} not found")

        return self._type_to_dto(type_by_id)

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
