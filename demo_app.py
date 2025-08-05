import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

# Load model
with open("receipt_forecast_model_xgb.pkl", "rb") as f:
    model = pickle.load(f)

# Month mapping
month_dict = {
    "January" : 1, "February":2 , "March":3 , "April":4, "May":5, "June":6, 
    "July":7, "August":8, "September":9, "October":10, "November":11, "December":12
}

def get_key(dictionary, target_value):
    return [key for key, value in dictionary.items() if value == target_value][0]

# Load data
data_daily = pd.read_csv("data_daily.csv")
data_daily['# Date'] = pd.to_datetime(data_daily['# Date'])
data_monthly = data_daily.groupby(data_daily['# Date'].dt.to_period("M"))['Receipt_Count'].sum().reset_index()
data_monthly.columns = ['Month', 'Receipt_Count']
data_monthly['Month'] = data_monthly['Month'].astype(str)

# Normalize data
max_val = data_monthly['Receipt_Count'].max()
min_val = data_monthly['Receipt_Count'].min()
data_normalized = (data_monthly['Receipt_Count'] - min_val) / (max_val - min_val)

# Prepare initial sequence
forecast = data_normalized[-3:].tolist()

# Layout
col1, col2 = st.columns(2)

with col1:
    # TODO: live code matplotlib figure
    pass

with col2:
    st.write(data_monthly)

# TODO: live code full sidebar including selectbox and forecasting loop
with st.sidebar:
    pass
