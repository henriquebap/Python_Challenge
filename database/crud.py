from fastapi import HTTPException
from fastapi.responses import JSONResponse
from database import SessionLocal, models
import schemas
from sqlalchemy.exc import IntegrityError


def create_user(user: schemas.UserCreate):
    db = SessionLocal()
    try:
        db_user = models.User()
        db_user.name = user.name
        db_user.last_name = user.last_name
        db_user.cpf = user.cpf
        db_user.email = user.email
        db_user.password = user.password
        db.add(db_user)
        db.commit()
    except IntegrityError:
        raise HTTPException(status_code=400, detail="CPF or email already registered")

    finally:
        db.close()

    return db_user


def read_user(user_id: int):
    db = SessionLocal()
    try:
        user = db.query(models.User).filter(models.User.id == user_id).first()
    finally:
        db.close()
    return user


def update_user(user_id: int, user: schemas.UserCreate):
    db = SessionLocal()
    try:
        db_user = db.query(models.User).filter(models.User.id == user_id).first()
        if user:
            db_user.name = user.name
            db_user.last_name = user.last_name
            db_user.cpf = user.cpf
            db_user.email = user.email
            db_user.password = user.password
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
    finally:
        db.close()

    return db_user


def delete_user(user_id: int):
    db = SessionLocal()
    try:
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
        return user
    finally:
        db.close()


def read_all_bikes_from_user(user_id):
    db = SessionLocal()
    try:
        items = db.query(models.Bike).filter(models.Bike.user_id == user_id).all()
        return items
    finally:
        db.close()


def read_user_by_cpf(cpf: str):
    db = SessionLocal()
    try:
        db_user = db.query(models.User).filter(models.User.cpf == cpf).first()
    finally:
        db.close()

    return db_user


def create_bike(user_id, bike: schemas.BikeCreate):
    db = SessionLocal()
    try:
        db_bike = models.Bike()
        db_bike.brand = bike.brand
        db_bike.serial_number = bike.serial_number
        db_bike.year = bike.year
        db_bike.value = bike.value
        db_bike.additional_modifications = bike.additional_modifications
        db_bike.user_id = user_id
        db.add(db_bike)
        db.commit()
        db.refresh(db_bike)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Numero de Serie ja resgistrado!")
    finally:
        db.close()
    return db_bike


def read_all_bikes():
    db = SessionLocal()
    try:
        artists = db.query(models.Bike).all()
    finally:
        db.close()
    return artists


# Função para ler uma bicicleta por número de série
def read_bike(bike_id: int):
    db = SessionLocal()
    try:
        bike = db.query(models.Bike).filter(models.Bike.id == bike_id).first()
        if bike:
            # Exibir as informações da bicicleta
            print("Marca:", bike.brand)
            print("Modelo:", bike.serial_number)
            print("Ano:", bike.year)
            print("Valor:", bike.value)
            # Exibir outras informações da bicicleta
            return bike
        else:
            print("Bicicleta não encontrada.")
            return None
    finally:
        db.close()


# Função para atualizar uma bicicleta
def update_bike_in_db(user_id: int, bike_id: int, bike: schemas.BikeCreate):
    db = SessionLocal()
    try:
        db_bike = db.query(models.Bike).filter(models.Bike.id == bike_id).first()
        if db_bike:
            db_bike.brand = bike.brand
            db_bike.serial_number = bike.serial_number
            db_bike.year = bike.year
            db_bike.value = bike.value
            db_bike.additional_modifications = bike.additional_modifications
            db.commit()
            db.refresh(db_bike)
            print("Bicicleta atualizada com sucesso.")
            return db_bike
        else:
            print("Bicicleta não encontrada.")
            return None
    finally:
        db.close()


# Função para deletar uma bicicleta por número de série
def delete_bike(bike_id):
    db = SessionLocal()
    try:
        db_bike = db.query(models.Bike).filter(models.Bike.id == bike_id).first()
        if db_bike:
            db.delete(db_bike)
            db.commit()
            print("Bike Removida com sucesso")
        return db_bike
    finally:
        db.close()


def create_image_prediction(prediction: schemas.ImagePredictionCreate):
    db = SessionLocal()
    try:
        db_prediction = models.ImagePrediction(**prediction.dict())
        db.add(db_prediction)
        db.commit()
        db.refresh(db_prediction)
    finally:
        db.close()

    return db_prediction
