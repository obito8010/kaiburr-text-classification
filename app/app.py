# app/app.py

import streamlit as st
import joblib
import numpy as np

# -----------------------------
# Load saved model and vectorizer
# -----------------------------
@st.cache_resource
def load_model():
    vectorizer = joblib.load("../model/tfidf_vectorizer.pkl")
    model = joblib.load("../model/logistic_regression_model.pkl")
    return vectorizer, model

tfidf, model = load_model()

# -----------------------------
# App Layout
# -----------------------------
st.set_page_config(page_title="Kaiburr Complaint Classifier", layout="centered")

st.title("💬 Kaiburr Complaint Text Classifier")
st.write("Enter a consumer complaint and let the model predict its category.")

# Input area
user_input = st.text_area("✍️ Paste complaint text here:", height=150)

if st.button("Predict Category"):
    if not user_input.strip():
        st.warning("Please enter a complaint first.")
    else:
        # Transform text using TF-IDF vectorizer
        input_features = tfidf.transform([user_input])
        prediction = model.predict(input_features)[0]

        # Label names mapping
        label_names = {
            0: "Credit Reporting",
            1: "Debt Collection",
            2: "Consumer Loan",
            3: "Mortgage"
        }

        st.success(f"🧠 Predicted Category: **{label_names[prediction]}**")

        st.info("Model: Logistic Regression (TF-IDF)\nAccuracy: 88.2%")
