from abc import ABCMeta, abstractmethod
from .dto import ExpensesCreateDTO, ExpensesDTO, TypeDTO, TypeCreateDTO


class ExpensesRepositoryInterface(metaclass=ABCMeta):

    @abstractmethod
    def create_expenses(self, create_expenses_dto: ExpensesCreateDTO) -> ExpensesDTO:
        pass

    @abstractmethod
    def create_type(self, create_type_dto: TypeCreateDTO) -> TypeDTO:
        pass

    # @abstractmethod
    # def get_expenses(self, ):


class ExpensesServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def create_expenses(self, create_expenses_dto: ExpensesCreateDTO) -> ExpensesDTO:
        pass

    @abstractmethod
    def create_type(self, create_type_dto: TypeCreateDTO) -> TypeDTO:
        pass
