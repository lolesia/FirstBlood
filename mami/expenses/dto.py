from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class TypeDTO:
    id: int
    type: str


@dataclass(frozen=True)
class TypeCreateDTO:
    type: str


@dataclass(frozen=True)
class ExpensesDTO:
    id: int
    type: str
    name: str
    cost: int
    date: date
    comment: str


@dataclass(frozen=True)
class ExpensesCreateDTO:
    type: str
    name: str
    cost: int
    date: date
    comment: Optional[str] = None
