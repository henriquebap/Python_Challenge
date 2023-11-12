from pydantic import BaseModel
from typing import List, Union


class UserBase(BaseModel):
    first_name: str
    last_name: str
    cpf: str
    email: str
    password: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    user_id: int
    bikes: List["Bike"] = []


class BikeBase(BaseModel):
    brand: str
    year: int
    value: int
    serial_number: str
    owner: Union[User, "UserCreate"]
    additional_modifications: str


class BikeCreate(BikeBase):
    pass


class Bike(BikeBase):
    id: int
    owner: User
