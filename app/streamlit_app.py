import streamlit as st
import requests
import os


st.title("Cocktail Recommender 2.0!")

user_input = None

#api_url = "https://wcdmx034sl.execute-api.us-east-1.amazonaws.com/prod/demo"

api_url = os.environ.get("api_url")

user_input = st.text_input(label="Please write a cocktail name.").upper()


if user_input:
  
  st.markdown("**API URL is** {}".format(api_url))
  response = requests.post(api_url, json = user_input)
  response_ = response.json()["body"]
  st.markdown("**Given Cocktail3 is** {}".format(response_))
  
  

