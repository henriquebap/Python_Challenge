from pydantic import BaseModel
from typing import List
from typing import Optional


class BikeBase(BaseModel):
    brand: str
    serial_number: str
    year: int
    value: float
    additional_modifications: str


class BikeCreate(BikeBase):
    pass


class Bike(BikeBase):
    id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    name: str
    last_name: str
    cpf: str
    email: str
    password: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class ImagePredictionBase(BaseModel):
    image_path: str
    prediction_image_path: str
    predicted_class: Optional[str] = None
    confidence: Optional[float] = None


class ImagePredictionCreate(ImagePredictionBase):
    pass


class ImagePrediction(ImagePredictionBase):
    id: int

    class Config:
        orm_mode = True
