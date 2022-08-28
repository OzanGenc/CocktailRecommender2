import streamlit as st
import requests
import os
import pandas as pd
import matplotlib.pyplot as plt


st.title("Cocktail Recommender 2.0!")


embedding_button = st.radio(
  "Similarity will be calculated using either Ingredients or All Information about the cocktail.",
  ('Only Ingredients', 'All Information'))

if embedding_button == 'Only Ingredients':
  df = pd.read_pickle("./df_universal_embedded_ingredients.pkl")
  similarity_df = pd.read_pickle("./similarity_ingredients_df.pkl")

else:
  df = pd.read_pickle("./df_universal_embedded_content.pkl")
  similarity_df = pd.read_pickle("./similarity_content_df.pkl")
        
        

user_input = None

user_input = st.text_input(label="Please write a cocktail name.").upper()


if user_input:
  
  try:
        
    recommended_cocktails = similarity_df.loc[user_input].sort_values(ascending=False)[1:6]
    
    st.markdown("**Given Cocktail is** [{}]({})".format(user_input, df.loc[user_input]['link']))
    
    st.markdown("**Recommended Cocktails are**" )
    
    st.markdown("**[{}]({}) - :cocktail: - [{}]({}) - :tropical_drink: - [{}]({}) - :wine_glass: - [{}]({}) - :beer: - [{}]({})**".format(
            recommended_cocktails.index[0], df.loc[recommended_cocktails.index[0]]['link'], 
            recommended_cocktails.index[1], df.loc[recommended_cocktails.index[1]]['link'], 
            recommended_cocktails.index[2], df.loc[recommended_cocktails.index[2]]['link'],
            recommended_cocktails.index[3], df.loc[recommended_cocktails.index[3]]['link'],
            recommended_cocktails.index[4], df.loc[recommended_cocktails.index[4]]['link']))
    
    
    fig, ax = plt.subplots()
    ax.barh(recommended_cocktails.index, recommended_cocktails.values)
    ax.invert_yaxis()
    ax.set_title('Similarities to given cocktail')
    st.pyplot(fig)
    
  except:
  
    try:
      # input api_url directly to the post method, don't assign it to a variable. DELETE this line.
      #api_url = os.environ.get("api_url")
      response = requests.post(api_url, json = user_input)
      response_ = response.json()["body"]
      st.markdown("**Given Cocktail is** {}".format(response_))
      
    except:
      st.markdown("**Embedding model currently is not in service, use [first version of the application](https://cocktail-recommender.herokuapp.com/).**")
      
  
  

