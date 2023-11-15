from sqlalchemy import Column, Integer, String, ForeignKey, CLOB, Float
from database import Base
from sqlalchemy.orm import relationship


# Cria o modelo de Usuario, passando os valores
class User(Base):
    __tablename__ = "USERS_BIKE5"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50))
    cpf = Column(String(14), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    bikes = relationship("Bike", back_populates="user", foreign_keys="Bike.user_id")


# Cria o modelo de bicicleta passando os valores
class Bike(Base):
    __tablename__ = "BIKES_CH4"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("USERS_BIKE5.id"))
    brand = Column(String(50), nullable=False)
    serial_number = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    value = Column(Float, default=0, nullable=False)
    additional_modifications = Column(CLOB)

    user = relationship("User", back_populates="bikes")
    image_predictions = relationship("ImagePrediction", back_populates="bike")


# Cria um modelo para a imagem retornada da API
class ImagePrediction(Base):
    __tablename__ = "IMAGE_PREDICTIONS"

    id = Column(Integer, primary_key=True, index=True)
    image_path = Column(String, index=True)
    prediction_image_path = Column(String, index=True)
    predicted_class = Column(String)
    confidence = Column(Float)
    bike_id = Column(Integer, ForeignKey("BIKES_CH4.id"))

    bike = relationship("Bike", back_populates="image_predictions")
