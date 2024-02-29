from dataclasses import dataclass


@dataclass(frozen=True)
class UserRegistrationDTO:
    email: str
    password: str
    profile_type: str
    first_name: str


@dataclass(frozen=True)
class UserDTO:
    id: int
    email: str
    phone: str
    is_active: bool
