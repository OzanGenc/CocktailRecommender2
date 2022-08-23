import streamlit as st
import requests


st.title("Cocktail Recommender 2.0!")

user_input = None

api_url = "https://wctppk9gul.execute-api.us-east-1.amazonaws.com/deploy_demo"

user_input = st.text_input(label="Please write a cocktail name.").upper()


todo = user_input
response = requests.put(api_url, json=todo)

if user_input:
  st.markdown("**Given Cocktail is** {}".format(response.json()))

