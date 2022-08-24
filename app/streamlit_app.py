import streamlit as st
import requests
import os

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

st.title("Cocktail Recommender 2.0!")

user_input = None

#api_url = "https://wcdmx034sl.execute-api.us-east-1.amazonaws.com/prod/demo"

api_url = os.environ.get("api_url")

user_input = st.text_input(label="Please write a cocktail name.").upper()


if user_input:
  
  response = requests.post(api_url, json = user_input)
  response_ = response.json()["body"]
  st.markdown("**Given Cocktail3 is** {}".format(response_))
  
  

