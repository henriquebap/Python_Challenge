from pydantic import BaseModel
from typing import List


class BikeTypeBase(BaseModel):
    name: str
    description: str


class BikeTypeCreate(BikeTypeBase):
    pass


class BikeType(BikeTypeBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True


# bike type schema


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
    owner: User
    additional_modifications: str
    biketype: BikeType


class BikeCreate(BikeBase):
    pass


class Bike(BikeBase):
    id: int
    owner: User

    class Config:
        orm_mode = True
