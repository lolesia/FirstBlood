from abc import ABCMeta, abstractmethod
from .dto import ExpensesCreateDTO, ExpensesDTO, TypeDTO, TypeCreateDTO


class ExpensesRepositoryInterface(metaclass=ABCMeta):

    @abstractmethod
    def get_expenses_by_id(self, expenses_id: int) -> ExpensesDTO:
        pass

    @abstractmethod
    def get_expenses_by_groomer_id(self, groomer_id: int) -> ExpensesDTO:
        pass

    @abstractmethod
    def create_expenses(self, create_expenses_dto: ExpensesCreateDTO) -> ExpensesDTO:
        pass

    @abstractmethod
    def get_type_by_id(self, type_id: int) -> TypeDTO:
        pass

    @abstractmethod
    def create_type(self, create_type_dto: TypeCreateDTO) -> TypeDTO:
        pass


class ExpensesServiceInterface(metaclass=ABCMeta):

    @abstractmethod
    def get_expenses_by_id(self, expenses_id: int) -> ExpensesDTO:
        pass

    @abstractmethod
    def get_expenses_by_groomer_id(self, groomer_id: int) -> ExpensesDTO:
        pass

    @abstractmethod
    def create_expenses(self, create_expenses_dto: ExpensesCreateDTO) -> ExpensesDTO:
        pass

    @abstractmethod
    def create_type(self, create_type_dto: TypeCreateDTO) -> TypeDTO:
        pass

    @abstractmethod
    def get_type_by_id(self, type_id: int) -> TypeDTO:
        pass
