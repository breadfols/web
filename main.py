from pydantic import BaseModel
from typing import List
from fastapi import FastAPI, HTTPException 
import uvicorn 
 
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

@app.get("/coffe/") 
def read_coffe(): return coffe_db

@app.get("/coffe/{id}")
def read_coffe(id: int):
    for coffe in coffe_db:
        if coffe.id == id:
            return coffe
    raise HTTPException(status_code=404, detail="Кофе не найден")

@app.get("/coffe-info/") 
def read_coffe_info(): return coffe_info_db

@app.get("/coffe-info/{id}")
def read_coffe_info(id: int): 
    for coffe_info in coffe_info_db: 
        if coffe_info.id == id: 
            return coffe_info 
    raise HTTPException(status_code=404, detail="Информация о кофе не найдена")

@app.get("/user/") 
def read_user(): return user_db

@app.get("/user/{id}") 
def read_user(id: int): 
    for user in user_db: 
        if user.id == id: 
            return user
    raise HTTPException(status_code=404, detail="Пользователь не найден")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)