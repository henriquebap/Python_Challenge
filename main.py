from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

import schemas
from database import crud


app = FastAPI()


@app.post("/users", status_code=201, response_model=schemas.User)
def create_user(user: schemas.UserCreate):
    db_user = crud.create_user(user)
    return db_user


@app.get("/users/{user_id}", response_model=list[schemas.User])
def get_user(user_id: int):
    user = crud.read_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Store not found")
    return user


@app.get("/users/{cpf}", response_model=schemas.User)
def get_user_id(cpf: str):
    user = crud.read_user_by_cpf(cpf)
    if not user:
        raise HTTPException(status_code=404, detail="CPF not found")
    return user


@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate):
    db_user = crud.update_user(user_id, user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    deleted_user = crud.delete_user(user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User successfully removed"}

@app.post("/users/{user_id}/bikes/", status_code=201, response_model=schemas.)