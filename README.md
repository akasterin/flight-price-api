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

class:
0 -> Economy;
1 -> Business

airline:
0 -> SpiceJet;
1 -> AirAsia;
2 -> Vistara;
3 -> GO_FIRST;
4 -> Indigo;
5 -> Air_India

stops:
0 -> zero;
1 -> one;
2 -> two_or_more

source_city:
0 -> Delhi;
1 -> Mumbai;
2 -> Bangalore;
3 -> Kolkata;
4 -> Hyderabad;
5 -> Chennai

destination_city:
0 -> Mumbai;
1 -> Bangalore;
2 -> Kolkata;
3 -> Hyderabad;
4 -> Chennai;
5 -> Delhi

departure_time:
0 -> Evening;
1 -> Early_Morning;
2 -> Morning;
3 -> Afternoon;
4 -> Night;
5 -> Late_Night

arrival_time:
0 -> Night;
1 -> Morning;
2 -> Early_Morning;
3 -> Afternoon;
4 -> Evening;
5 -> Late_Night

