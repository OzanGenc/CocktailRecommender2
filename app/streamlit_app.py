import streamlit as st
import requests
import os
import pandas as pd
import matplotlib.pyplot as plt

'''
Follow instructions from here in order to create API Gateway. 

https://shreyansh26.github.io/post/2022-01-23_model_deployment_using_aws_lambda/


Create Lambda function from scratch. On Heroku reveal config vars insert api_url without "" (quotes).
The Lambda function --> 

import json

def lambda_handler(event, context):
    # TODO implement
    
    response = event + " hello from lambda_handler"
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }



'''

df = pd.read_pickle("./df_universal_embedded.pkl")
similarity_df = pd.read_pickle("./similarity_df.pkl")

st.title("Cocktail Recommender 2.0!")


user_input = None

# input api_url directly to the post method, don't assign it to a variable. DELETE this line.
#api_url = os.environ.get("api_url")

user_input = st.text_input(label="Please write a cocktail name.").upper()




if user_input:
  
  #try:
        
  recommended_cocktails = similarity_df.loc[user_input.upper()].sort_values(ascending=False)[1:6]
    
  st.markdown("**Given Cocktail is** [{}]({})".format(user_input.upper(), 'https://cocktailpartyapp.com/'))
    
  st.markdown("**Recommended Cocktails are** [{}]({}), [{}]({}), [{}]({}), [{}]({}), [{}]({})".format(
        recommended_cocktails.index[0], 'https://cocktailpartyapp.com/', 
        recommended_cocktails.index[1], 'https://cocktailpartyapp.com/', 
        recommended_cocktails.index[2], 'https://cocktailpartyapp.com/',
        recommended_cocktails.index[3], 'https://cocktailpartyapp.com/',
        recommended_cocktails.index[4], 'https://cocktailpartyapp.com/'))
    
    
  fig, ax = plt.subplots()
  ax.barh(recommended_cocktails.index, recommended_cocktails.values)
  ax.invert_yaxis()
  ax.set_title('Similarities to given cocktail')
  st.pyplot(fig)
  '''
  except:
  
    response = requests.post(api_url, json = user_input)
    response_ = response.json()["body"]
    st.markdown("**Given Cocktail is** {}".format(response_))
  
  '''

