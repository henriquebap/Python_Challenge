from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text,
    ForeignKey,
)
from database import Base
from datetime import datetime
from sqlalchemy.orm import relationship


class BikeType(Base):
    __tablename__ = "BIKETYPES_CH"

    bike_type_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)

    bikes = relationship("Bike", back_populates="bike_type")


class User(Base):
    __tablename__ = "USERS_BIKE"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    cpf = Column(String(14), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    bikes = relationship("Bike", back_populates="user")


class Bike(Base):
    __tablename__ = "BIKES_CH"

    bike_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("USERS_BIKE.user_id"), nullable=False)
    bike_type_id = Column(
        Integer, ForeignKey("BIKETYPES_CH.bike_type_id"), nullable=False
    )
    brand = Column(String(50), nullable=False)
    serial_number = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    value = Column(Integer, nullable=False)
    additional_modifications = Column(Text)

    user = relationship("User", back_populates="bikes")
    bike_type = relationship("BikeType", back_populates="bikes")
