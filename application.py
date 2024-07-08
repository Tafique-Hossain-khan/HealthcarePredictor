import streamlit as st
from src.Diabetes.pipeline.prediction_pipeline import CustomInput, Prediction
from streamlit_option_menu import option_menu
'''
st.sidebar.title("Medical app")
st.sidebar.image('https://cdn-icons-png.flaticon.com/512/124/124945.png')
diabetes_button = st.sidebar.button('Diabetes')
heart_button = st.sidebar.button('Heart')
symptoms_button = st.sidebar.button('Predict Symptoms')
'''
with st.sidebar:
    selected = option_menu('Medical app',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Dieseas prediction Based on symptioms'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

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
        prediction = perform_prediction()
        if prediction == 1:
            st.write("You have diabetes please consult a doctor ")
        else:
            st.write("You don't have diabetes! Take care")


## page for hear dese prediction
if heart_button:
    st.write("project commig soon   ")



'''



import streamlit as st
#code for displaying item from the lsit
# List of items
items = ["a", "b", "c", "d"]

# Create a string to display the items with numbers
items_str = "\n".join([f"{i+1}. {item}" for i, item in enumerate(items)])

# Display the items in a box
st.text_area("Items List", items_str, height=150, max_chars=None)

# Alternatively, you can use st.markdown to display with some styling
st.markdown("**Items List**")
st.markdown(f"```{items_str}```")
'''