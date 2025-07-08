import streamlit as st
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

st.set_page_config(page_title="Sales Forecast Dashboard", layout="wide")
st.title("📈 Sales Forecasting Dashboard")

uploaded_file = st.file_uploader("Upload your CSV file with 'Date' and 'Sales' columns", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df = df.rename(columns={'Date': 'ds', 'Sales': 'y'})
    df['ds'] = pd.to_datetime(df['ds'])
    df = df.sort_values('ds')

    st.subheader("📊 Raw Data Preview")
    st.dataframe(df.tail())

    period = st.slider("Select forecast period (days):", min_value=30, max_value=365, value=90, step=30)

    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=period)
    forecast = model.predict(future)

    st.subheader("🔮 Prophet Forecast Plot")
    fig1 = model.plot(forecast)
    st.pyplot(fig1)

    st.subheader("📈 Forecast Components")
    fig2 = model.plot_components(forecast)
    st.pyplot(fig2)

    df['timestamp'] = df['ds'].map(pd.Timestamp.toordinal)
    X = df[['timestamp']]
    y = df['y']
    reg = LinearRegression().fit(X, y)
    y_pred = reg.predict(X)

    st.subheader("📉 Linear Regression Trend")
    fig3, ax = plt.subplots()
    ax.plot(df['ds'], df['y'], label='Actual Sales')
    ax.plot(df['ds'], y_pred, label='Trend (Regression)', color='red')
    ax.set_title('Sales Trend Analysis')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig3)

    mse = mean_squared_error(y, y_pred)
    st.markdown(f"### 🧮 Regression MSE: `{mse:.2f}`")
else:
    st.info("Please upload a CSV file to begin. Example format: Date, Sales")