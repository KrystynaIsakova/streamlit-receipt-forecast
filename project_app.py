import xgboost as xgb
import streamlit as st
import joblib
import pandas as pd
from matplotlib import pyplot as plt

model = joblib.load('xgboost_model.pkl')
data = pd.read_csv('data_clean.csv')

st.title('Corporacion Favorita Sales Forecasting')

store_nbr = st.selectbox('Select Store Id', data['store_nbr'].unique())
data_filtered = data[data['store_nbr']==store_nbr]


item_nbr = st.selectbox('Select Item Id',data_filtered['item_nbr'].unique())
data_filtered = data_filtered[data_filtered['item_nbr']==item_nbr]

if st.button('Get Forecast'):

  prediction = model.predict(data_filtered.drop(['unit_sales', 'date'], axis=1))
  prediction_df = pd.DataFrame({'date': data_filtered['date'],
                                'prediction': prediction})
  '''
  fig, ax = plt.subplots()
  ax.plot(prediction_df['date'], prediction_df['prediction'])
  ax.set_xlabel('Date')
  ax.set_ylabel('Sales')
  ax.set_title('Sales Forecast')
  st.pyplot(fig)
  '''
  st.write(prediction_df)