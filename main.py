from pydantic import BaseModel
from typing import List
from fastapi import FastAPI, HTTPException 
import uvicorn 

# Определение моделей
class Coffe(BaseModel): 
    id: int 
    name: str 
    price: float

class CoffeInfo(BaseModel): 
    id: int 
    title: str 
    text: str

class User(BaseModel): 
    id: int 
    name: str
    email: str

# Базы данных (временные)
coffe_db = [
    Coffe(id=1, name="Американо", price=100.0),
    Coffe(id=2, name="Эспрессо", price=80.0),
    Coffe(id=3, name="Капучино", price=120.0),
]

coffe_info_db = [
    CoffeInfo(id=1, title="Американо", text="Американо - это кофе, приготовленный из эспрессо и горячей воды."),
    CoffeInfo(id=2, title="Латте", text="Латте - это кофе, приготовленный из эспрессо и молока."),
    CoffeInfo(id=3, title="Эспрессо", text="Эспрессо - это кофе, приготовленный из молотых кофейных зерен."),
]

user_db = [
    User(id=1, name="Иван Иванов", email="ivan@example.com"),
    User(id=2, name="Петр Петров", email="petr@example.com"),
    User(id=3, name="Сергей Сергеев", email="sergey@example.com"),
]

app = FastAPI()

# CRUD для Coffe
@app.get("/coffe/", response_model=List[Coffe]) 
def read_coffe(): 
    return coffe_db

@app.get("/coffe/{id}", response_model=Coffe)
def read_coffe(id: int):
    for coffe in coffe_db:
        if coffe.id == id:
            return coffe
    raise HTTPException(status_code=404, detail="Кофе не найден")

@app.post("/coffe/", response_model=Coffe)
def create_coffe(coffe: Coffe):
    coffe_db.append(coffe)
    return coffe

@app.put("/coffe/{id}", response_model=Coffe)
def update_coffe(id: int, updated_coffe: Coffe):
    for index, coffe in enumerate(coffe_db):
        if coffe.id == id:
            coffe_db[index] = updated_coffe
            return updated_coffe
    raise HTTPException(status_code=404, detail="Кофе не найден")

@app.delete("/coffe/{id}")
def delete_coffe(id: int):
    for index, coffe in enumerate(coffe_db):
        if coffe.id == id:
            del coffe_db[index]
            return {"detail": "Кофе удален"}
    raise HTTPException(status_code=404, detail="Кофе не найден")

# CRUD для CoffeInfo
@app.get("/coffe-info/", response_model=List[CoffeInfo]) 
def read_coffe_info(): 
    return coffe_info_db

@app.get("/coffe-info/{id}", response_model=CoffeInfo) 
def read_coffe_info(id: int): 
    for coffe_info in coffe_info_db: 
        if coffe_info.id == id: 
            return coffe_info 
    raise HTTPException(status_code=404, detail="Информация о кофе не найдена")

@app.post("/coffe-info/", response_model=CoffeInfo)
def create_coffe_info(coffe_info: CoffeInfo):
    coffe_info_db.append(coffe_info)
    return coffe_info

@app.put("/coffe-info/{id}", response_model=CoffeInfo)
def update_coffe_info(id: int, updated_coffe_info: CoffeInfo):
    for index, coffe_info in enumerate(coffe_info_db):
        if coffe_info.id == id:
            coffe_info_db[index] = updated_coffe_info
            return updated_coffe_info
    raise HTTPException(status_code=404, detail="Информация о кофе не найдена")

@app.delete("/coffe-info/{id}")
def delete_coffe_info(id: int):
    for index, coffe_info in enumerate(coffe_info_db):
        if coffe_info.id == id:
            del coffe_info_db[index]
            return {"detail": "Информация о кофе удалена"}
   