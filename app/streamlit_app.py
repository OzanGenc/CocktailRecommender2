import streamlit as st


st.title("Cocktail Recommender 2.0!")

user_input = None
user_input = st.text_input(label="Please write a cocktail name.").upper()

if user_input:
  name = "Mai Tai"
  st.markdown("**Given Cocktail is** {}".format(name))

