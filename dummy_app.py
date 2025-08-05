import streamlit as st

st.title("🔮 Dummy Receipt Forecaster")

month = st.selectbox("Choose a month:", [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
])

forecast = len(month) * 1000

st.write(f"You selected: {month}")
st.write(f"Forecast: {forecast} receipts")
