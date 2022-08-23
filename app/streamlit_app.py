import streamlit as st


st.title("Streamlit <-> Heroku Template App")


# if button clicked, classify
if st.button("Get Next Random Digit"):
    # get random image from the test set
    prediction = 5

    # classify
    
    st.text("Predicted to be  : {}".format(prediction)
    
