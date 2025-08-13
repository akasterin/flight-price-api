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

```json
{
"class_": 0,
"duration": 2.5,
"days_left": 15,
"airline": 3,
"stops": 1,
"destination_city": 4,
"source_city": 2,
"arrival_time": 5,
"departure_time": 1
}
```

```plaintext
"class_": 0             → 🎟 Класс: 0 = Business
"duration": 2.5         → ⏱ Длительность полёта: 2.5 часа
"days_left": 15         → 📅 Дней до вылета: 15
"airline": 3            → 🛫 Авиалиния: 3 = IndiGo
"stops": 1              → 🔄 Пересадки: 1 = одна пересадка
"destination_city": 4   → 🎯 Город назначения: 4 = Kolkata
"source_city": 2        → 🏙 Город вылета: 2 = Delhi
"arrival_time": 5       → ⏰ Время прибытия: 5 = Ночь
"departure_time": 1     → 🛫 Время вылета: 1 = Раннее утро
```

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

# ✈️ Прогноз цен на авиабилеты (End-to-End ML + MLOps + Data Engineering)

## 📄 Описание проекта
Проект представляет собой **сервис для прогнозирования цен на авиабилеты** по заданным параметрам.  
Модель обучена на исторических данных о перелётах и развёрнута в виде API (FastAPI) и Telegram-бота.

---

## 📌 Основные этапы реализации

1. **📥 Сбор данных**
   - Источник: [Kaggle — Flight Price Prediction Dataset](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction)
   - Формат: CSV
   - Инструменты: **Pandas** для загрузки и первичного анализа

2. **🧹 Обработка данных (ETL)**
   - ETL (*Extract, Transform, Load*) — извлечение, преобразование и загрузка данных
   - Обработка пропусков, кодирование категориальных признаков в числовые
   - Масштабирование признаков, работа с выбросами

3. **🧠 Обучение модели**
   - Основная модель: `RandomForestRegressor` из **scikit-learn**  
     - Подбор гиперпараметров через `GridSearchCV`
   - Также протестирована модель **XGBoostRegressor** (градиентный бустинг по деревьям)  
     - Настройка параметров (`max_depth`, `n_estimators`, `learning_rate` и др.)
     - Показала близкие или лучшие метрики, чем RandomForest
   - Сохранение модели в формате `.pkl` через **joblib**

4. **🌐 Развёртывание API**
   - Использован **FastAPI**
   - Реализованы эндпоинты:
     - `/predict` — получение прогноза цены
     - `/` — тестовый эндпоинт
   - Приложение развернуто на [Render](https://render.com)

5. **🤖 Telegram-бот**
   - Написан с использованием библиотеки **python-telegram-bot**
   - Пошаговое заполнение параметров с помощью **ConversationHandler**
   - Вызов API `/predict` для выдачи результата
   - Бот работает локально(не выгружен)*

---

## 🛠 Использованные технологии

| Компонент         | Технология / Инструмент | Описание |
|-------------------|------------------------|----------|
| Язык программирования | Python 3.11 | Основной язык |
| Анализ данных     | Pandas, NumPy | Обработка и анализ |
| Модели ML         | scikit-learn (RandomForestRegressor), **XGBoost** | Построение и тестирование моделей |
| API               | FastAPI | Веб-интерфейс модели |
| Сериализация      | joblib | Сохранение и загрузка модели |
| Хостинг API       | Render | Деплой API |
| Бот               | python-telegram-bot | Telegram-интерфейс |
| IDE               | Jupyter Notebook, VS Code | Разработка |
| Данные            | Kaggle ([ссылка](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction)) | Датасет для обучения |

---

## 📌 Возможности улучшения проекта

1. **📦 Контейнеризация и деплой**
   - Добавить **Docker** для упаковки приложения в контейнер
   - Настроить автоматический деплой через **GitHub Actions (CI/CD)**
   - Разместить API через **GCP** или **AWS**

2. **⚙️ Автоматизация процессов**
   - Внедрить **Apache Airflow** для автоматизации ETL-процессов и переобучения модели

3. **📊 Улучшение модели**
   - Провести финальное сравнение **XGBoost** и RandomForest на боевых данных
   - Протестировать **LightGBM**
   - Добавить **MLflow** для отслеживания экспериментов

4. **💬 Интеграция**
   - Расширить Telegram-бота кнопками выбора значений
   - Сделать веб-интерфейс на **Streamlit** или **Gradio**

5. **📈 Мониторинг**
   - Внедрить **Prometheus + Grafana** для мониторинга работы API

---

## 📚 Термины

- **ETL (Extract, Transform, Load)** — извлечение, преобразование и загрузка данных
- **CI/CD** — автоматическая проверка и публикация изменений
- **Docker** — упаковка приложения и зависимостей в контейнер
- **MLflow** — управление экспериментами машинного обучения
- **Apache Airflow** — планировщик и автоматизатор задач
- **Prometheus** — сбор метрик
- **Grafana** — визуализация метрик
- **XGBoost** — библиотека для градиентного бустинга по деревьям, часто показывает высокие результаты в табличных данных

---

## 🔗 Полезные ссылки

- 📊 Датасет: [Kaggle — Flight Price Prediction Dataset](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction)
- 🌐 Хостинг API: [Render](https://render.com)

