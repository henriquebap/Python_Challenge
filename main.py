from fastapi import FastAPI, HTTPException, UploadFile, File, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import ia_preditc
import schemas
from database import crud

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    message = "Olá, Para uma melhor interação, acesse a documentação."
    return templates.TemplateResponse(
        "index.html", {"request": request, "message": message}
    )


@app.get("/documentation", include_in_schema=False)
async def custom_swagger_ui_html(request: Request):
    return templates.TemplateResponse(
        "redoc.html", {"request": request, "endpoints": app.routes}
    )


# Outros endpoints...

# O restante do seu código...


# Metodo post para mensagem
@app.post(
    "/users",
    status_code=201,
    response_model=schemas.User,
    summary="Criar um novo usuario",
)
# Funcao criar o usuario
def create_user(user: schemas.UserCreate):
    # Mensagem para o usuario
    """
    Area para criar um novo usuario \n
    ! Se atente em colocar as entradas e informacoes corretas !
    """
    db_users = crud.create_user(user)
    return db_users


# Metodo Get que le o usuario por ID
@app.get("/users/{user_id}", response_model=schemas.User)
def get_user_by_id(user_id: int):
    user = crud.read_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user


# Metodo PUT que chama o usuario por ID e chama funcao para atualizar
@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate):
    db_user = crud.update_user(user_id, user)
    if not db_user:
        raise HTTPException(status_code=404, detail="user not found")

    return db_user


# Metodo DELETE, chama user por ID e depois da validacao ele chama a funcao para excluir o usuario
@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user_by_id(user_id: int):
    user = crud.read_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")

    crud.delete_user(user_id)

    message = {"message": "User deletado com sucesso"}
    return JSONResponse(content=message)


# metodo POST de criar bike, valida o user id, depois chama a funcao para criar a bike
@app.post("/users/{user_id}/bikes/", status_code=201, response_model=schemas.Bike)
def create_bike(user_id: int, bike: schemas.BikeCreate):
    user = crud.read_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")

    db_bike = crud.create_bike(user_id, bike)
    return db_bike


# Metodo GET para ler bikes por ID
@app.get("/bikes/{bike_id}", response_model=schemas.Bike)
def get_bike(bike_id: int):
    bike = crud.read_bike(bike_id)
    if not bike:
        raise HTTPException(status_code=404, detail="bike not found")
    return bike


# Metodo PUT para atualizar uma bike, valida pelo ID da bike e o ID do usuario
@app.put("/bikes/{bike_id}", response_model=schemas.Bike)
def update_bike(bike_id: int, user_id: int, bike: schemas.BikeCreate):
    db_bike = crud.update_bike_in_db(user_id, bike_id, bike)
    if not db_bike:
        raise HTTPException(status_code=404, detail="Bicicleta não encontrada")

    return db_bike


# Metodo DEL que le um ID de bicicleta e se for verdadeiro finaliza a funcao DEL
@app.delete("/bikes/{bike_id}", response_model=schemas.Bike)
def delete_bike_by_id(bike_id: int):
    bike = crud.read_bike(bike_id)
    if not bike:
        raise HTTPException(status_code=404, detail="bike not found")

    crud.delete_bike(bike_id)

    message = {"message": "bike deleted"}
    return JSONResponse(content=message)


# Pega todas as bikes de cada Usuario
@app.get("/users/{user_id}/bikes/", response_model=list[schemas.Bike])
def get_bike_from_user(user_id: int):
    user = crud.read_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    bikes = crud.read_all_bikes_from_user(user_id)
    return bikes


# LE todas as bikes do banco de dados
@app.get("/bikes", response_model=list[schemas.Bike])
def get_bike():
    bikes = crud.read_all_bikes()
    return bikes


# Metodo POST, ele cria um bota para o usuario enviar uma imagem ( Feito assim para simular a requisao de abrir a camera )
# Depois ele chama a API e salva o retorno da API no banco de dados utilizando o CRUD


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
