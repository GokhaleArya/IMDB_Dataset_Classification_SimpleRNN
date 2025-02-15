# Importing libraries and loading the model
import numpy as np
from tensorflow.keras.datasets import imdb
from tensorflow.keras.utils import pad_sequences
from tensorflow.keras.models import load_model

# Load the IMDB dataset word index
word_index = imdb.get_word_index()
reverse_word_index = {value : key for key,value in word_index.items()}

# Load the pre trained model
model = load_model('simple_rnn_imdb.h5')

# Helper functions
# Function to decode reviews
def decode_review(encode_review):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in encode_review])

def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = pad_sequences([encoded_review], maxlen=500)
    return padded_review

def predict_sentiment(review):
    preprocessed_input = preprocess_text(review)
    prediction = model.predict(preprocessed_input)
    sentiment = "Positive" if prediction[0][0]>0.5 else "Negative"
    return sentiment, prediction[0][0]

# Streamlit app
import streamlit as st

st.title('IMDB Movie Review Sentiment Analysis')
st.write("Enter a movie review to classify it as positive or negative.")
# User input
user_input = st.text_area("Movie Review", placeholder="Enter your movie review here....")

if st.button('Classify'):
    if user_input:
        sent, pred = predict_sentiment(user_input)
        st.write(f"Sentiment : {sent}")
        st.write(f"Prediction Score : {pred}")

    else:
        st.write("Please enter a movie review!")
