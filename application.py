import streamlit as st
from src.Diabetes.pipeline.prediction_pipeline import CustomInput, Prediction


# CSS for styling and animation
css = """
<style>
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
.intro {
    animation: fadeIn 2s;
    color: #2E86C1;
    font-size: 1.2em;
    font-family: Arial, sans-serif;
    padding: 20px;
    border: 2px solid #AED6F1;
    border-radius: 10px;
    background-color: #E8F8F5;
}
.header {
    animation: fadeIn 2s;
    color: #154360;
    font-size: 2em;
    font-family: Arial, sans-serif;
    text-align: center;
    margin-top: 20px;
}
</style>
"""

# App description with custom CSS and animation
st.write(css, unsafe_allow_html=True)
st.markdown("<div class='header'>Health Prediction App</div>", unsafe_allow_html=True)
st.markdown("""
<div class='intro'>
    Welcome to the Health Prediction App. This app allows you to predict various health conditions such as Diabetes, Heart Disease,
    and provides a symptom-based disease predictor. Please select an option from the sidebar to get started.
</div>
""", unsafe_allow_html=True)

# Create a placeholder for dynamic content
placeholder = st.empty()

st.sidebar.title("Medical app")
st.sidebar.image('https://animationvisarts.com/wp-content/uploads/2016/11/Olympics-Logo.jpg')
diabetes_button = st.sidebar.button('Diabetes')
heart_button = st.sidebar.button('Heart')
symptoms_button = st.sidebar.button('Predict Symptoms')

if diabetes_button:

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


## page for hear dese prediction
if heart_button:
    st.write("project commig soon   ")