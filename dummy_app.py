import streamlit as st
st.title("Dummy App")

month = st.selectbox("Choose a month",
             ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"])


st.write(f"You have selected {month}")