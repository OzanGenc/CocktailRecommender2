import streamlit as st
import requests
import os
import pandas as pd
import matplotlib.pyplot as plt
import requests
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image

st.title("Cocktail Recommender 2.0!")


st.markdown("Cocktail Recommender 2.0 is an improved version of [Cocktail Recommender](https://cocktail-recommender.herokuapp.com/). It is a tool that recommends cocktails based on provided name, ingredients or description of a cocktail using Artificial Intelligence.")
st.markdown("You can provide name of a cocktail (e.g. Margarita) to find similar cocktails to it, you can write ingedients (e.g. Vodka, Orange juice) or you can describe (e.g. fruity, refreshing) what kind of cocktail you would like to enjoy, and get recommendations based on that.")
st.markdown("Cheers :tropical_drink:")

df = pd.read_pickle("./df_universal_embeddings.pkl")

embedding_button = st.radio(
  "Similarity will be calculated using either Ingredients or All Information about the cocktail.",
  ('Only Ingredients --> Choose this option if you provide only ingredients', 'Descriptions --> Choose this option if you provide a cocktail description with ingredients'))

if embedding_button == 'Only Ingredients --> Choose this option if you provide only ingredients':
  embedding_type = 'ingredients_embeddings'
  similarity_df = pd.read_pickle("./similarity_ingredients_df.pkl")

else:
  embedding_type = 'content_embeddings'
  similarity_df = pd.read_pickle("./similarity_content_df.pkl")
        
        
user_input = None

user_input = st.text_input(label="Please write a cocktail name, ingredients, or a cocktail description.").upper()



#----------------------

if user_input == 'I LOVE YOU BABY KO':
  image = Image.open('./babyko.png')
  st.image(image, use_column_width=True)
  st.markdown("**I love you too baby ko :black_heart:**" )

#------------------------



if user_input:
  
  try:
        
    recommended_cocktails = similarity_df.loc[user_input].sort_values(ascending=False)[1:6]
    
    st.markdown("**Given Cocktail is** [{}]({})".format(user_input, df.loc[user_input]['link']))
    
    st.markdown("**Recommended Cocktails are**" )
    
    st.markdown("**[{}]({}) - :cocktail: - [{}]({}) - :tropical_drink: - [{}]({}) - :wine_glass: - [{}]({}) - :tumbler_glass: - [{}]({})**".format(
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
    
      response = requests.post(os.environ.get("api_url"), json = user_input)
      user_input_embedding = response.json()["body"]

      Y = [float(item) for item in user_input_embedding[1:-1].split(',')]
      Y = np.array(Y).reshape(1, -1)
      
      
      similarity_to_user_input = pd.DataFrame(index=df.index)

      cos_sim_list = []

      for index, row in df.iterrows():
        X = np.array(row[embedding_type]).reshape(1, -1)
        cos_sim = cosine_similarity(X, Y)
        cos_sim_list.append(cos_sim[0][0])

        
      similarity_to_user_input['similarity'] = cos_sim_list
        
      recommended_cocktails = similarity_to_user_input.sort_values(by='similarity', ascending=False)[:5]
      
      
    
      st.markdown("**Recommended Cocktails are**" )
    
      st.markdown("**[{}]({}) - :cocktail: - [{}]({}) - :tropical_drink: - [{}]({}) - :wine_glass: - [{}]({}) - :tumbler_glass: - [{}]({})**".format(
            recommended_cocktails.index[0], df.loc[recommended_cocktails.index[0]]['link'], 
            recommended_cocktails.index[1], df.loc[recommended_cocktails.index[1]]['link'], 
            recommended_cocktails.index[2], df.loc[recommended_cocktails.index[2]]['link'],
            recommended_cocktails.index[3], df.loc[recommended_cocktails.index[3]]['link'],
            recommended_cocktails.index[4], df.loc[recommended_cocktails.index[4]]['link']))
    
    
      fig, ax = plt.subplots()
      ax.barh(recommended_cocktails.index, recommended_cocktails['similarity'].values)
      ax.invert_yaxis()
      ax.set_title('Similarities to given description')
      st.pyplot(fig)
      
      
    except:
      st.markdown("**The given cocktail couldn't be found in the database. Also, the embedding model is not currently in service, please use the [first version of the application](https://cocktail-recommender.herokuapp.com/).**")
      
      
  
