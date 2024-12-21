import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import streamlit as st
import warnings
import datetime

warnings.filterwarnings("ignore")

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv("yahoo_stock.csv", parse_dates=['Date'], index_col='Date')
    return data

data = load_data()

# Streamlit app interface
st.title("Stock Price Prediction (SARIMAX)")

# Select a date for prediction from the dataset
date_input = st.date_input("Select a date for prediction", datetime.date(2018, 1, 1))
sample_date = pd.to_datetime(date_input)

if sample_date not in data.index:
    st.error("Selected date is not available in the dataset.")
else:
    # Split the data into train and test sets based on the selected date
    train_size = data.index.get_loc(sample_date)
    train = data.iloc[:train_size][['Close']]
    test = data.iloc[train_size:][['Close']]

    # Define the order and seasonal order for the SARIMAX model
    order = (1, 1, 1)
    seasonal_order = (1, 1, 1, 12)

    # Specify the number of steps to forecast ahead
    HORIZON = 5
    st.write(f'Forecasting horizon: {HORIZON} days')

    # Make predictions on the test data
    training_window = 120  # Increased window size to capture more data
    history = list(train['Close'])[-training_window:]

    predictions = []
    for t in range(min(HORIZON, len(test))):
        model = SARIMAX(history, order=order, seasonal_order=seasonal_order)
        model_fit = model.fit(disp=False)

        yhat = model_fit.forecast(steps=1)
        predictions.append(yhat[0])

        history.append(test['Close'].iloc[t])
        history = history[-training_window:]

    # Calculate RMSE
    if len(predictions) > 0:
        rmse = np.sqrt(mean_squared_error(test['Close'][:len(predictions)], predictions))
        st.write(f'RMSE: {rmse}')

        # Plot the results
        plt.figure(figsize=(12, 6))
        plt.plot(train.index, train['Close'], label='Train')
        plt.plot(test.index[:len(predictions)], test['Close'][:len(predictions)], label='Test')
        plt.plot(test.index[:len(predictions)], predictions, label='Predictions')
        plt.legend()
        plt.title(f'Stock Price Prediction (SARIMAX) from {sample_date.date()}')
        st.pyplot(plt.gcf())
    else:
        st.write("Not enough data to make predictions for the selected date.")