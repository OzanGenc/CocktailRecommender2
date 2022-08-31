# Cocktail Recommender 2

This repository contains Jupyter notebooks for web scraping and batch transforming cocktail descriptions to numerical values as well as Python files for deploying the recommender system as a web app. 

1. Beautiful Soup was used to scrape data from https://cocktailpartyapp.com/.
2. Pre-trained [BERT Large Universal Sentence Encoder](https://aclanthology.org/2021.emnlp-main.502/) model is used which is deployed using AWS Sagemaker Jumpstart. It was trained using 'Wikipedia and BookCorpus datasets' and it can be found at [TensorFlow Hub](https://tfhub.dev/google/universal-sentence-encoder-cmlm/en-large/1). The pre-trained transformer model converts any text input (name, ingredients, and/or description of a cocktail) to a vector having dimensions of (1024,1). Cosine similarities of vectorized cocktail descriptions are calculated to compare semantic similarities between the cocktails.  
3. AWS Lambda function deployed to invoke the endpoint model.
4. REST API was created using Amazon API Gateway. This enables us to send POST requests to our Lambda function in a secure way. 

You can use the system [here](https://cocktailrecommender2.herokuapp.com/)

You can learn more about the system reading this blog post.
