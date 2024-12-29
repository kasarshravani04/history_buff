import streamlit as st
import requests

st.title("Welcome all to history buff!")
st.header("Just add the date and I will find out what happened on that day in history.")

choosed_date = st.date_input("Choose Date", value="today", min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, format="YYYY/MM/DD", disabled=False, label_visibility="visible")
# st.button("Submit", type="primary")

if st.button("Submit", type="primary"):
    month = choosed_date.strftime("%m")
    day = choosed_date.strftime("%d")

    # API URL
    url = f"http://numbersapi.com/{month}/{day}/date"

    # Send request
    response = requests.get(url)

    # Check response
    if response.status_code == 200:
        # print(f"On this day: {response.text}")
        st.write(f"On this day: {response.text}")
    else:
        # print(f"Error: {response.status_code}")
        st.write(f"Error: {response.status_code}")