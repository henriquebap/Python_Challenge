from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
import ia_preditc

import schemas
from database import crud

app = FastAPI()


@app.post(
    "/users",
    status_code=201,
    response_model=schemas.User,
    summary="Criar um novo usuario",
)
def create_user(user: schemas.UserCreate):
    """
    Area para criar um novo usuario \n
    ! Se atente em colocar as entradas e informacoes corretas !
    """
    db_users = crud.create_user(user)
    return db_users


@app.get("/users/{user_id}", response_model=schemas.User)
def get_user_by_id(user_id: int):
    user = crud.read_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user


@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate):
    db_user = crud.update_user(user_id, user)
    if not db_user:
        raise HTTPException(status_code=404, detail="user not found")

    return db_user


@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user_by_id(user_id: int):
    user = crud.read_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")

    crud.delete_user(user_id)

    message = {"message": "User deletado com sucesso"}
    return JSONResponse(content=message)


@app.post("/users/{user_id}/bikes/", status_code=201, response_model=schemas.Bike)
def create_bike(user_id: int, bike: schemas.BikeCreate):
    user = crud.read_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")

    db_bike = crud.create_bike(user_id, bike)
    return db_bike


@app.get("/bikes/{bike_id}", response_model=schemas.Bike)
def get_bike(bike_id: int):
    bike = crud.read_bike(bike_id)
    if not bike:
        raise HTTPException(status_code=404, detail="bike not found")
    return bike


@app.put("/bikes/{bike_id}", response_model=schemas.Bike)
def update_bike(bike_id: int, user_id: int, bike: schemas.BikeCreate):
    db_bike = crud.update_bike_in_db(user_id, bike_id, bike)
    if not db_bike:
        raise HTTPException(status_code=404, detail="Bicicleta não encontrada")

    return db_bike


@app.delete("/bikes/{bike_id}", response_model=schemas.Bike)
def delete_bike_by_id(bike_id: int):
    bike = crud.read_bike(bike_id)
    if not bike:
        raise HTTPException(status_code=404, detail="bike not found")

    crud.delete_bike(bike_id)

    message = {"message": "bike deleted"}
    return JSONResponse(content=message)


@app.get("/users/{user_id}/bikes/", response_model=list[schemas.Bike])
def get_bike_from_user(user_id: int):
    user = crud.read_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    bikes = crud.read_all_bikes_from_user(user_id)
    return bikes


@app.get("/bikes", response_model=list[schemas.Bike])
def get_bike():
    bikes = crud.read_all_bikes()
    return bikes


@app.post("/predict-bike-image", response_model=schemas.ImagePrediction)
async def predict_bike_image(
    file: UploadFile = File(...),
):
    image_path, prediction_image_path, predicted_class, confidence = ia_preditc.cv_api(
        file.file
    )

    # Salvar no banco de dados
    db_prediction = crud.create_image_prediction(
        schemas.ImagePredictionCreate(
            image_path=image_path,
            prediction_image_path=prediction_image_path,
            predicted_class=predicted_class,
            confidence=confidence,
        ),
    )

    return db_prediction
