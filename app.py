import streamlit as st
import requests

'''
# TaxiFareModel front
'''


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

st.write(f'Your fare will be ${int(prediction)}')

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
