# 🧾 Receipt Forecasting App

This is a simple Streamlit web app that forecasts **monthly receipt counts** using historical data from 2021 and an XGBoost model.

---

## 🚀 Features

- Interactive receipt count forecasting for any month in 2022  
- Historical data visualization  
- Built with `Streamlit`, `pandas`, `matplotlib`, and `XGBoost`

---

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/KrystynaIsakova/streamlit-receipt-forecast.git
cd streamlit-receipt-forecast
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the app:**
```bash
streamlit run app.py
```

## 📁 Files
* `app.py` – main Streamlit app
* `data_daily.csv` – raw data (daily receipt counts)
* `receipt_forecast_model_xgb.pkl` – trained XGBoost model
* `requirements.txt` – required Python libraries
