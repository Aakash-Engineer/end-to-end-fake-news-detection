import joblib
import pandas as pd
import streamlit as st
from FakeNewsDetection.pipeline.prediction import Prediction

# Set page configuration
st.set_page_config(
    page_title="Fake News Detection",
    page_icon="📰",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Add title and description
st.title("Fake News Detection 📰")
st.markdown("""
Welcome to the **Fake News Detection** app. Enter a news article below and click **Predict** to determine whether it's real or fake.
""")

# Load the vectorizer and model
vectorizer = joblib.load("models/vectorizer.pkl")
model = joblib.load("models/model.pkl")

# Display model information in the sidebar
st.sidebar.title("Model Information")
st.sidebar.markdown("""
- **Model:** Logistic Regression
- **Vectorizer:** TF-IDF
- **Accuracy:** 98%
- **Features:** 200
""")

# Initialize session state to manage the prediction state
if 'prediction' not in st.session_state:
    st.session_state.prediction = None

# User input
user_input = st.text_area("Enter news text here", height=200)

# Clear the prediction result when the user input changes
if user_input == "":
    st.session_state.prediction = None

if st.button("Predict"):
    if user_input.strip():
        # Transform the input text
        user_input_df = Prediction([user_input]).preprocess()
        input_vect = vectorizer.transform(user_input_df['text'])
        # Predict using the loaded model
        prediction = model.predict(input_vect)
        # Store the prediction in session state
        st.session_state.prediction = prediction[0]
    else:
        st.warning("Please enter the news text.")

# Display the result based on the prediction state
if st.session_state.prediction == 0:
    st.success("The news is **Real**.")
elif st.session_state.prediction == 1:
    st.error("The news is **Fake**.")