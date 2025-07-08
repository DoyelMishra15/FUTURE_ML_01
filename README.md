# 📈 Sales Forecasting Dashboard

This project is an interactive Streamlit dashboard for forecasting sales trends using historical data. It combines **Facebook Prophet** for time series forecasting and **Linear Regression** for trend analysis.

---

## 🔧 Features

- Upload your own CSV file (`Date`, `Sales`)
- Forecast future sales using Prophet
- Visualize seasonality components (weekly, monthly trends)
- Analyze sales trend using linear regression
- Interactive UI via Streamlit

---

## 🖥️ Sample Screenshots

### 🔮 Prophet Forecast Plot
![Forecast Plot](prophet_forecast_plot.png)

### 📊 Forecast Components (Trend & Seasonality)
![Forecast Components](forecast_components.png)

### 📉 Regression MSE
![MSE](Regression_MSE.png)

### 📈 Sales Trend Analysis with Linear Regression
![Linear Regression](linear_regression_trend.png)

---

## 🗂️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/sales-forecast-dashboard.git
cd sales-forecast-dashboard
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app
```bash
streamlit run app.py
```

---

## 🧪 Sample Data Format

```
Date,Sales
2023-01-01,200
2023-01-02,210
...
```

You can use the included `sample_sales_data.csv` to try it out quickly.

---

## 📦 Tech Stack

- **Python**
- **Streamlit**
- **Prophet**
- **scikit-learn**
- **matplotlib**
- **pandas**

---
