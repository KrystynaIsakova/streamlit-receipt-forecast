import streamlit as st
import pandas as pd
import numpy as np

st.title('My first streamlit app!')
name = st.text_input("Enter your name")

st.write(f'Hello, {name}!')
age = st.slider('What is your age?', 0, 100, 25)
st.write(f'You are {age} years old.')

color = st.selectbox('Choose your favorite color!',
             ['Red', 'Green', 'Blue', 'Yellow'])

if st.button('Submit'):
    st.success(f'Hello, {name}! You are {age} years old and your favorite color is {color}.')

st.subheader('Simple Data Display')
data = pd.DataFrame(np.random.randn(10,3), columns=['A', 'B', 'C'])
data['category'] = np.random.choice(['X', 'Y', 'Z'], size=10)
st.dataframe(data)

st.subheader('Line Chart')
st.line_chart(data.drop('category', axis=1))


category = st.selectbox('Select category', data['category'].unique())
data_filtered = data.query('category == @category')
st.dataframe(data_filtered)
st.line_chart(data_filtered.drop('category', axis=1))