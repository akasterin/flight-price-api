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

    
    
  🔢 Таблица соответствий закодированных значений (для API)
  
✈️ Airline (авиалиния):

    0 — AirAsia

    1 — Air India

    2 — GO FIRST

    3 — Indigo

    4 — SpiceJet

    5 — Vistara

🌆 Source City (город вылета):

    0 — Bangalore

    1 — Chennai

    2 — Delhi

    3 — Hyderabad

    4 — Kolkata

    5 — Mumbai

🏙️ Destination City (город прилёта):

    0 — Bangalore

    1 — Chennai

    2 — Delhi

    3 — Hyderabad

    4 — Kolkata

    5 — Mumbai

🕑 Departure Time (время вылета):

    0 — Afternoon

    1 — Early Morning

    2 — Evening

    3 — Late Night

    4 — Morning

    5 — Night

🕓 Arrival Time (время прилёта):

    0 — Afternoon

    1 — Early Morning

    2 — Evening

    3 — Late Night

    4 — Morning

    5 — Night

🛑 Stops (количество пересадок):

    0 — One

    1 — Two or more

    2 — Zero

💺 Class (класс обслуживания):

    0 — Business

    1 — Economy
