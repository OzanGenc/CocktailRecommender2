import streamlit as st
import requests


st.title("Cocktail Recommender 2.0!")

user_input = None

api_url = "https://wcdmx034sl.execute-api.us-east-1.amazonaws.com/prod/demo"

user_input = st.text_input(label="Please write a cocktail name.").upper()


#myobj = "vodka"

#response = requests.request("POST", api_url, data=user_input)

if user_input:
  
  myjob = user_input
  response = requests.post(api_url, json = myobj)
  response_ = response.json()["body"]
  st.markdown("**Given Cocktail3 is** {}".format(response_))
  #st.markdown("**Given Cocktail2 is** {}".format(response.json()))
  

