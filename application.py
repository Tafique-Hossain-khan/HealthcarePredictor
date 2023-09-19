import streamlit as st
from src.pipeline.prediction_pipeline import CustomInput,Prediction

st.header("Diabetes Predictor")

gender_list = ['Male',"Female"]
gender = st.selectbox("Gender",gender_list)
age = st.text_input('Age')
hypertension = st.selectbox('High Blood pressure',['YES','NO'])
if hypertension == 'YES':
    hypertension = 1
else :
    hypertension =0

heart_disease = st.selectbox('Heart Dises',['YES','NO'])
if heart_disease == 'YES':
    heart_disease = 1
else :
    heart_disease = 0

smoking_history = st.selectbox("Smoking History",["never", "former", "current", "not current", "ever"])
bmi = st.number_input("BMI")
HbA1c_level = st.text_input('HbA1c_level	')
blood_glucose_level = st.text_input('blood_glucose_level')

def perform_prediction():
    obj = CustomInput(gender,age,hypertension,heart_disease,smoking_history,bmi,HbA1c_level,blood_glucose_level)
    featers = obj.get_df()
    predict_obj = Prediction()
    price = predict_obj.predict(featers)
    return price
submit_button = st.button("Submit")
if submit_button:
    st.write(f'The price of Diamond is:{perform_prediction()}')
