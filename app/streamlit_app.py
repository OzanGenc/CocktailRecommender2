import streamlit as st
import requests


st.title("Cocktail Recommender 2.0!")

user_input = None

api_url = " https://rhlxfhbjqj.execute-api.us-east-1.amazonaws.com/default/myLambdaDemo"

user_input = st.text_input(label="Please write a cocktail name.").upper()




response = requests.request("POST", api_url, data={user_input})

if user_input:
  st.markdown("**Given Cocktail is** {}".format(response.json()))

