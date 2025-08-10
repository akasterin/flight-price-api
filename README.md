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
  
## 📊 Таблица соответствия параметров для API `/predict`

| 🏷 Поле         | 📖 Описание параметра               | 🔢 Возможные значения / диапазон |
|-----------------|------------------------------------|------------------------------------|
| 🎟 `class_`     | Класс перелёта                     | `0` ✈ Business, `1` 💺 Economy |
| ⏱ `duration`   | Длительность полёта (часы)         | От `0.83` до `49.83` ⏳ |
| 📅 `days_left`  | Дней до вылета                     | Целое число, напр. `3` 📆 |
| 🛫 `airline`    | Авиакомпания                       | `0` 🟥 AirAsia, `1` 🇮🇳 Air_India, `2` 🟦 GO_FIRST, `3` 🟢 IndiGo, `4` 🟨 SpiceJet, `5` 🟪 Vistara |
| 🔄 `stops`      | Кол-во пересадок                   | `0` 🚀 zero, `1` 🛑 one, `2` 🔁 two_or_more |
| 🎯 `destination_city` | Город назначения           | `0` 🏙 Bangalore, `1` 🏙 Chennai, `2` 🏙 Delhi, `3` 🏙 Hyderabad, `4` 🏙 Kolkata, `5` 🏙 Mumbai |
| 🏙 `source_city`| Город вылета                       | `0` 🏙 Bangalore, `1` 🏙 Chennai, `2` 🏙 Delhi, `3` 🏙 Hyderabad, `4` 🏙 Kolkata, `5` 🏙 Mumbai |
| ⏰ `arrival_time`| Время прибытия                    | `0` 🌇 Afternoon, `1` 🌅 Early_Morning, `2` 🌆 Evening, `3` 🌃 Late_Night, `4` 🌄 Morning, `5` 🌙 Night |
| 🛫 `departure_time`| Время вылета                   | `0` 🌇 Afternoon, `1` 🌅 Early_Morning, `2` 🌆 Evening, `3` 🌃 Late_Night, `4` 🌄 Morning, `5` 🌙 Night |


