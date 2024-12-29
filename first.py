import streamlit as st

st.title("Welcome all to history buff!")
st.header("Just add the date and I will find out what happened on that day in history.")

choosed_date = st.date_input("Choose Date", value="today", min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, format="YYYY/MM/DD", disabled=False, label_visibility="visible")

print(choosed_date)