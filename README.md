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

## 📦 Пример запроса:\

{<br>
  "class_": 0,           // 🎟 Класс: 0 = Business<br>
  "duration": 2.5,       // ⏱ Длительность полёта: 2.5 часа<br>
  "days_left": 15,       // 📅 Дней до вылета: 15<br>
  "airline": 3,          // 🛫 Авиалиния: 3 = IndiGo<br>
  "stops": 1,            // 🔄 Пересадки: 1 = одна пересадка<br>
  "destination_city": 4, // 🎯 Город назначения: 4 = Kolkata<br>
  "source_city": 2,      // 🏙 Город вылета: 2 = Delhi<br>
  "arrival_time": 5,     // ⏰ Время прибытия: 5 = Late_Night (поздняя ночь)<br>
  "departure_time": 1    // 🛫 Время вылета: 1 = Morning (утро)<br>
}<br>
    
## 📊 Таблица соответствия параметров для API `/predict`

| 🏷 Поле              | 📖 Описание параметра       | 🔢 Возможные значения / диапазон |
|----------------------|----------------------------|-----------------------------------|
| 🎟 `class_`          | Класс перелёта              | - `0` ✈ Business  <br> - `1` 💺 Economy |
| ⏱ `duration`         | Длительность полёта (часы) | - От `0.83` до `49.83` ⏳ |
| 📅 `days_left`       | Дней до вылета              | - Целое число, напр. `3` 📆 |
| 🛫 `airline`         | Авиакомпания                | - `0` 🟥 AirAsia  <br> - `1` 🇮🇳 Air_India  <br> - `2` 🟦 GO_FIRST  <br> - `3` 🟢 IndiGo  <br> - `4` 🟨 SpiceJet  <br> - `5` 🟪 Vistara |
| 🔄 `stops`           | Кол-во пересадок            | - `0` 🚀 zero  <br> - `1` 🛑 one  <br> - `2` 🔁 two_or_more |
| 🎯 `destination_city`| Город назначения            | - `0` 🏙 Bangalore  <br> - `1` 🏙 Chennai  <br> - `2` 🏙 Delhi  <br> - `3` 🏙 Hyderabad  <br> - `4` 🏙 Kolkata  <br> - `5` 🏙 Mumbai |
| 🏙 `source_city`     | Город вылета                | - `0` 🏙 Bangalore  <br> - `1` 🏙 Chennai  <br> - `2` 🏙 Delhi  <br> - `3` 🏙 Hyderabad  <br> - `4` 🏙 Kolkata  <br> - `5` 🏙 Mumbai |
| ⏰ `arrival_time`    | Время прибытия              | - `0` 🌇 Afternoon  <br> - `1` 🌅 Early_Morning  <br> - `2` 🌆 Evening  <br> - `3` 🌃 Late_Night  <br> - `4` 🌄 Morning  <br> - `5` 🌙 Night |
| 🛫 `departure_time`  | Время вылета                | - `0` 🌇 Afternoon  <br> - `1` 🌅 Early_Morning  <br> - `2` 🌆 Evening  <br> - `3` 🌃 Late_Night  <br> - `4` 🌄 Morning  <br> - `5` 🌙 Night |


