import streamlit as st
import requests
import pandas as pd

'''
# Taxi fare price predictor
'''

st.markdown('''
### **"It's something i guess"** 
### - *random people*

_______________
''')


date = st.date_input("date and time")
time = st.time_input("time")
pickup_latitude = st.number_input("pickup latitude", value=40.74)
pickup_longitude = st.number_input("pickup longitude", value=-73.98)
dropoff_latitude = st.number_input("dropoff latitude", value=40.80)
dropoff_longitude = st.number_input("dropoff longitude", value=-73.95)
passenger_count = st.number_input('passenger count', value=2, min_value=1, max_value=8)


url_api = 'https://taxifare.lewagon.ai/predict'

params = {
    "pickup_datetime" :  f'{date} {time}',
    "pickup_longitude" : pickup_longitude,
    "pickup_latitude" : pickup_latitude,
    "dropoff_longitude" : dropoff_longitude,
    "dropoff_latitude" : dropoff_latitude,
    "passenger_count" : passenger_count
}

response = requests.get(url_api, params=params).json()

prediction = response['prediction']

st.markdown(f'''
_______________

## Your fare will be ${int(prediction)}
_______________
''')


if st.checkbox('Show map', False):
    df = pd.DataFrame(
            [
                [pickup_latitude, pickup_longitude],
                [dropoff_latitude, dropoff_longitude]
            ],
            columns = ['lat', 'lon']
        )
    st.map(df)




# CSS = """
# h1 {
#     color: black;
# }
# .stApp {
#     background-color: #ba93b6;
#     background-size: cover;
# }
# """

# st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


