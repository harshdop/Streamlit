# File: test_streamlit.py

import streamlit as st
import requests

api_key= "1ff308b1e8msha2a439eac2cc3f9p1fd81ajsnbb88c025e9e8"
st.title("Google Tranlator")
st.write("This is to test my Streamlit setup.")  




text = st.text_input(label="Enter your query which you want to convert to hindi", key="input_text")


def translater(input_text):
    url = "https://google-translator9.p.rapidapi.com/v2"

    

    payload = {
        "q": input_text,
        "source": "en",
        "target": "pa",
        "format": "text"
    }
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "google-translator9.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()
    output = data['data']['translations'][0]['translatedText']
    
    return output
output = translater(text)
st.write(output)