# 💬 Kaiburr Text Classification (Task 5 – Data Science)

**Candidate: CHINMAY SASEENDRAN** 
**Submission Date:** [20/10/2025]

----------------------------------------------------------

## 🧠 Project Overview

This project is built as part of the **Kaiburr Recruitment Assessment (Task 5 – Data Science)**.  
The goal is to classify **consumer complaint texts** into one of four categories using machine learning and natural language processing (NLP) techniques.

**Categories:**
1. Credit Reporting  
2. Debt Collection  
3. Consumer Loan  
4. Mortgage  

-----------------------------------------------------------

## 🚀 Project Phases

| Phase | Description | Status |
|-------|--------------|--------|
| **1. Setup** | Project folder structure, environment, Git initialization | ✅ Completed |
| **2. Data Cleaning** | Read, clean, and balance dataset (≈20k rows, 5k/class) | ✅ Completed |
| **3. Model Training** | Train multiple models (Logistic Regression, Naive Bayes, Random Forest) |✅ Completed |
| **4. Streamlit App** | Deploy best model for live predictions | ✅ Completed |

-----------------------------------------------------------

## 📁 Project Structure
kaiburr-text-classification/
│
├── app/
│ └── app.py
│
├── data/
│ └── consumer_complaints_sample_balanced.csv
│
├── model/
│ ├── logistic_regression_model.pkl
│ └── tfidf_vectorizer.pkl
│
├── notebooks/
│ ├── data_cleaning.ipynb
│ ├── eda_analysis.ipynb
│ └── model_training.ipynb
│
├── screenshots/
│ ├── eda_wordclouds.png
│ ├── model_accuracy_chart.png
│ ├── confusion_matrix.png
│ ├── streamlit_ui.png
│ └── streamlit_prediction.png
│
├── README.md
├── requirements.txt
└── .gitignore

-----------------------------------------------------------

## Phase 1 – Data Cleaning Summary

- Cleaned and combined large complaint CSV file in chunks  
- Filtered 4 major complaint types  
- Balanced each class to **5,000 samples** (20,000 total)  
- Saved final dataset as `consumer_complaints_sample_balanced.csv`

 **Tools used:** `pandas`, `numpy`  
 **Techniques:** chunk reading, text cleaning, class balancing, sampling  

-----------------------------------------------------------

## Phase 2 – Model Training & Evaluation

| Model | Accuracy |
|--------|-----------|
| Logistic Regression | **88.2%** |
| Naive Bayes | 84.7% |
| Random Forest | 80.1% |

 **Best Model:** Logistic Regression (TF-IDF features)  
 **Vectorizer:** TF-IDF (`max_features=5000`, bigrams)  
 **Artifacts Saved:**  
- `/model/tfidf_vectorizer.pkl`  
- `/model/logistic_regression_model.pkl`

**Visuals:**
- Confusion Matrix  
- Accuracy Comparison Chart  

> Logistic Regression achieved 88.2% accuracy, showing strong performance on this 4-class problem.

-----------------------------------------------------------


## Phase 3 – Streamlit Web App

### Run Locally

```bash
cd app
streamlit run app.py

Then open http://localhost:8501 in your browser.

# Features

Input a complaint text

Predicts one of four categories instantly

Displays model details and confidence

Example

Input: “I found incorrect information on my credit report and the company refused to fix it.”

Output: Predicted Category: Credit Reporting

-----------------------------------------------------------

## Screenshots


-----------------------------------------------------------

# Technologies Used
Category	            Tools
Language	            Python 3.10
Libraries	            pandas, scikit-learn, matplotlib, seaborn, nltk, joblib, wordcloud, streamlit
Modeling	            TF-IDF + Logistic Regression
Visualization	        Matplotlib, Seaborn, WordCloud
Deployment	            Streamlit

-----------------------------------------------------------

Possible Future Enhancements

* Fine-tune Logistic Regression hyperparameters
* Use BERT or other transformer-based embeddings
* Deploy the Streamlit app to Streamlit Cloud or Hugging Face Spaces
* Add real-time data ingestion (live complaint API)

-----------------------------------------------------------

## Final Remarks

This project demonstrates the complete lifecycle of a data science task:

Data → Cleaning → EDA → Model Training → Deployment.

Accuracy Achieved: 88.2%
Best Model: Logistic Regression (TF-IDF)

Quality of both code and documentation has been maintained as per Kaiburr’s evaluation criteria.