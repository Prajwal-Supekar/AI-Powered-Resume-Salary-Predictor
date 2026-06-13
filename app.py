import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("salary_model.pkl", "rb"))

st.title("Salary Predictor")

age = st.slider("Age", 18, 60, 25)
gender = st.selectbox("Gender", ["Male", "Female"])
education = st.selectbox("Education Level", ["Bachelor's", "Master's", "PhD"])
job = st.text_input("Job Title", "Data Analyst")
experience = st.slider("Years of Experience", 0, 30, 2)

if st.button("Predict Salary"):

    # ✅ DEFINE DATA INSIDE BUTTON
    data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'Education Level': [education],
        'Job Title': [job],
        'Years of Experience': [experience]
    })

    prediction = model.predict(data)

    st.success(f"Predicted Salary: ₹{prediction[0]:,.2f}")