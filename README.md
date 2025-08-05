# ✈️ Flight Price Prediction API

Это API предсказывает стоимость авиабилета по следующим параметрам:

- Класс: Economy / Business
- Время в пути (в минутах)
- Кол-во дней до вылета
- Авиалиния
- Количество пересадок
- Город отправления и прибытия
- Время отправления и прибытия

## 🔗 Ссылка на API:
https://flight-price-api-cxaq.onrender.com/docs

## 📦 Пример запроса:

{
  "class_": 0,
  "duration": 0,
  "days_left": 0,
  "airline": 2,
  "stops": 1,
  "destination_city": 4,
  "source_city": 0,
  "arrival_time": 2,
  "departure_time": 3
}

Расшифровка:

    class_ = 0 → Business
    airline = 2 → GO_FIRST
    stops = 1 → two_or_more
    destination_city = 4 → Kolkata
    source_city = 0 → Bangalore
    arrival_time = 2 → Evening
    departure_time = 3 → Late_Night

