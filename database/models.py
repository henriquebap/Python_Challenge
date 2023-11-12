from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, CLOB
from database import Base
from datetime import datetime
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "USERS_BIKE1"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50))
    cpf = Column(String(14), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    bikes = relationship("Bike", back_populates="user")


class Bike(Base):
    __tablename__ = "BIKES_CH"
    bike_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("USERS_BIKE1.user_id"))
    brand = Column(String(50), nullable=False)
    serial_number = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    value = Column(Integer, nullable=False)
    additional_modifications = Column(CLOB)

    user = relationship("User", back_populates="bikes")


# class PredictionResult(Base):
#     __tablename__ = "API_RESULTS"
#     id = Column(Integer, primary_key=True)
#     image_path = Column(String(255), nullable=False)
#     prediction_image_path = Column(String(255), nullable=False)
#     predicted_class = Column(String(50))
#     confidence = Column(Integer)
#     additional_info = Column(CLOB)
#     bike_id = Column(Integer, ForeignKey("BIKES_CH.bike_id"))

#     # Define a many-to-one relationship to bikes
#     bike = relationship("Bike", back_populates="api_results")

#     def __init__(
#         self,
#         image_path,
#         prediction_image_path,
#         predicted_class,
#         confidence,
#         additional_info,
#     ):
#         self.image_path = image_path
#         self.prediction_image_path = prediction_image_path
#         self.predicted_class = predicted_class
#         self.confidence = confidence
#         self.additional_info = additional_info
