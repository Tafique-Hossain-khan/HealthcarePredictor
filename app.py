import streamlit as st

from src.Diabetes.pipeline.prediction_pipeline import CustomInput, Prediction


# Initialize session state variables
if 'diabetes' not in st.session_state:
    st.session_state.diabetes = False
if 'heart' not in st.session_state:
    st.session_state.heart = False
if 'predict_symptoms' not in st.session_state:
    st.session_state.predict_symptoms = False

# Sidebar components
st.sidebar.title("Medical app")
st.sidebar.image('https://cdn-icons-png.flaticon.com/512/124/124945.png')

diabetes_button = st.sidebar.button('Diabetes')
heart_button = st.sidebar.button('Heart')
symptoms_button = st.sidebar.button('Predict Symptoms')

# Update session state based on button clicks
if diabetes_button:
    st.session_state.diabetes = True
    st.session_state.heart = False
    st.session_state.predict_symptoms = False

if heart_button:
    st.session_state.heart = True
    st.session_state.diabetes = False
    st.session_state.predict_symptoms = False

if symptoms_button:
    st.session_state.predict_symptoms = True
    st.session_state.diabetes = False
    st.session_state.heart = False

# Diabetes Predictor Page
if st.session_state.diabetes:
    st.header("Diabetes Predictor")

    gender_list = ['Male', "Female"]
    gender = st.selectbox("Gender", gender_list, key="gender")
    age = st.text_input('Age', key="age")
    hypertension = st.selectbox('High Blood pressure', ['YES', 'NO'], key="hypertension")
    heart_disease = st.selectbox('Heart Disease', ['YES', 'NO'], key="heart_disease")
    smoking_history = st.selectbox("Smoking History", ["never", "former", "current", "not current", "ever"], key="smoking_history")
    bmi = st.number_input("BMI", key="bmi")
    HbA1c_level = st.text_input('HbA1c_level', key="HbA1c_level")
    blood_glucose_level = st.text_input('blood_glucose_level', key="blood_glucose_level")

    def perform_prediction():
        hypertension_value = 1 if st.session_state.hypertension == 'YES' else 0
        heart_disease_value = 1 if st.session_state.heart_disease == 'YES' else 0

        obj = CustomInput(st.session_state.gender, st.session_state.age, hypertension_value,
                          heart_disease_value, st.session_state.smoking_history, st.session_state.bmi,
                          st.session_state.HbA1c_level, st.session_state.blood_glucose_level)
        features = obj.get_df()
        predict_obj = Prediction()
        prediction = predict_obj.predict(features)
        return prediction

    submit_button = st.button("Submit", key="submit")
    if submit_button:
        prediction = perform_prediction()
        if prediction == 1:
            st.warning("You have diabetes please consult a doctor ")
        else:
            st.warning("You don't have diabetes! Take care")

# Heart Disease Prediction Page
if st.session_state.heart:
    st.write("Project coming soon")

# Predict Symptoms Page
if st.session_state.predict_symptoms:
    st.write("Predict Symptoms functionality coming soon")
