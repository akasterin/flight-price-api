from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
import numpy as np


#Создаем обьект приложения FastAPI
app = FastAPI()

MODEL_PATH = os.path.join(os.path.dirname(__file__), "../model.pkl")

# Загружаем сохраненную модель XGBoost
model = joblib.load(MODEL_PATH) # путь к файлу модели

# Описываем структуру входных данных через Pydantic
class FlightData(BaseModel):
    class_: int
    duration: float
    days_left: int
    airline: int
    stops: int
    destination_city: int
    source_city: int
    arrival_time: int
    departure_time: int

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать! Открой /docs для API документации."}

# Главный эндпоинт, который принимает POST-запрос и отдает предсказание
@app.post("/predict")
def predict_price(data: FlightData):
    # преобразуем входные данные в numpy-массив с нужной формой
    input_array = np.array([[
        data.class_,
        data.duration,
        data.days_left,
        data.airline,
        data.stops,
        data.destination_city,
        data.source_city,
        data.arrival_time,
        data.departure_time
    ]])

    # Получаем предсказание от модели 
    prediction = model.predict(input_array)

    # возвращаем как JSON
    return {"predicted_price": round(float(prediction[0]),2)}


#from fastapi import FastAPI	Импорт FastAPI	Это веб-фреймворк
#from pydantic import BaseModel	Импорт модели валидации	Pydantic — для проверки данных
#import joblib	Импорт joblib	Чтобы загрузить модель из файла
#model = joblib.load(...)	Загрузка модели	Подгружаем model.pkl
#class FlightData(...)	Модель данных	Описывает, какие поля нужно получить в JSON
#@app.post("/predict")	Декоратор	Обрабатывает POST-запрос на адрес /predict
#predict_price(...)	Функция предсказания	Преобразует данные и вызывает predict