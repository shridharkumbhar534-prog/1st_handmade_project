import streamlit as st
import requests as re
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

st.set_page_config(page_title = 'My Weather App', page_icon='🌧️')

st.title('My Weather App 🌧️')

st.write("Enter the city name to get the current weather information.")

city = st.text_input("Enter the city name = ")

if st.button("fetch weather"):
    response = re.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
    data = response.json()
    if response.status_code == 200:
        # Extact information
         temperature = data['main']['temp']
         humidity = data['main']['humidity']
         wind_speed = data['wind']['speed']
         weather = data['weather'][0]['description']
         name = data['name']
         country = data['sys']['country']
         # st.write(f"Temperature: {temperature}°C")
         # st.write(f"Humidity: {humidity}%")
         # st.write(f"Wind Speed: {wind_speed} m/s")
         # st.write(f"Weather: {weather}")
         # st.write(f"City: {name}, Country: {country}")
         # st.metric(label="Temperature🌡️", value=f"{temperature}°C")
         # st.metric(label="Humidity💦", value=f"{humidity}%")
         # st.metric(label="Wind Speed💨", value=f"{wind_speed} m/s")
         # st.metric(label="Weather☁️", value=f"{weather}")
         # st.metric(label="City📍", value=f"{name}, {country}")
         st.subheader(f"{name}, {country}")
         # set colunmns
         col1, col2 = st.columns(2)
         col3, col4 = st.columns(2)
         col5, col6 = st.columns(2)
         col1.metric(label="Temperature", value=f"🌡️{temperature}°C")
         col2.metric(label="Humidity", value=f"💦{humidity}%")
         col3.metric(label="Weather", value=f"☁️{weather}")
         col4.metric(label="Wind Speed", value=f"💨{wind_speed} m/s")
         # col5.metric(label="Country", value=f"🚩{name}, {country}")
         # col6.metric(label="City", value=f"📍{name}, {country}")
         
    else:
        st.error("City not found. Please enter a valid city name.") 
        
        
        
