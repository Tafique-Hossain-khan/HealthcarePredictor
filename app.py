import streamlit as st

from src.Heart.pipeline.prediction_pipeline import PredictionHeart,CustomInputHeart
from src.Diabetes.pipeline.prediction_pipeline import CustomInput, Prediction
from src.Medication_system.recommend import prediction,recommendation
from streamlit_option_menu import option_menu


# Initialize session state variables
if 'diabetes' not in st.session_state:
    st.session_state.diabetes = False
if 'heart' not in st.session_state:
    st.session_state.heart = False
if 'predict_symptoms' not in st.session_state:
    st.session_state.predict_symptoms = False
if 'show_welcome' not in st.session_state:
    st.session_state.show_welcome = True  # Initialize welcome message state

## new side bar
with st.sidebar:
    selected = option_menu('Medical app',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Dieseas prediction Based on symptioms'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)
# Update session state based on button clicks
if selected == 'Diabetes Prediction' or selected == 'Heart Disease Prediction' or selected == 'Dieseas prediction Based on symptioms':
    st.session_state.show_welcome = False  # Hide welcome message on any button click

# Update session state based on button clicks
if selected == 'Diabetes Prediction':
    st.session_state.diabetes = True
    st.session_state.heart = False
    st.session_state.predict_symptoms = False

if selected == 'Heart Disease Prediction' :
    st.session_state.heart = True
    st.session_state.diabetes = False
    st.session_state.predict_symptoms = False

if selected == 'Dieseas prediction Based on symptioms':
    st.session_state.predict_symptoms = True
    st.session_state.diabetes = False
    st.session_state.heart = False

# Conditionally display the welcome message
if st.session_state.show_welcome:
    st.write("""
    ## Welcome to the Health App
    This project is a health app where you can predict your risk for diabetes and heart diseases,
    and get recommendations based on the symptoms of your conditions.
    """)


# Diabetes Predictor Page
if st.session_state.diabetes:
    st.header("Diabetes Predictor")

    gender_list = ['Male', "Female"]
    gender = st.selectbox("Gender", gender_list, key="gender")
    age = st.text_input('Age', key="age")
    hypertension = st.selectbox('High Blood pressure', ['YES', 'NO'], key="hypertension")
    heart_disease = st.selectbox('Heart Disease', ['YES', 'NO'], key="heart_disease")
    smoking_history = st.selectbox("Smoking History", ["never", "former", "current", "not current", "ever"], key="smoking_history")
    bmi = st.text_input("BMI", key="bmi")
    HbA1c_level = st.text_input('Hemoglobin A1c', key="HbA1c_level")
    blood_glucose_level = st.text_input('Blood Glucose Level', key="blood_glucose_level")

    def perform_prediction():
        # Check for empty inputs
        if not all([gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level]):
            st.warning("Please fill in all the details.")
            return None, None

        try:
            age_value = int(age)
            HbA1c_level_value = float(HbA1c_level)
            blood_glucose_level_value = int(blood_glucose_level)
            bmi_value = float(bmi)
        except ValueError:
            st.warning("Please enter valid numeric values for Age, HbA1c level, BMI, and Blood Glucose Level.")
            return None, None

        hypertension_value = 1 if hypertension == 'YES' else 0
        heart_disease_value = 1 if heart_disease == 'YES' else 0

        obj = CustomInput(gender, age_value, hypertension_value, heart_disease_value, smoking_history, bmi_value, HbA1c_level_value, blood_glucose_level_value)
        features = obj.get_df()
        predict_obj = Prediction()
        prediction = predict_obj.predict(features)
        return prediction, features

    submit_button = st.button("Submit", key="submit")
    if submit_button:
        prediction, features = perform_prediction()
        if prediction is not None:
            if prediction == 1:
                st.warning("You have diabetes, please consult a doctor.")
            else:
                st.warning("You don't have diabetes! Take care.")


# Heart Disease Prediction Page
if st.session_state.heart:
    
    # Title
    st.title('Heart Disease Predictor')

    # Input fields
    bmi = st.number_input('BMI', min_value=10.0, max_value=50.0, step=0.1)
    sleep_time = st.number_input('SleepTime', min_value=0, max_value=24, step=1)

    smoking = st.selectbox('Smoking', ['No', 'Yes'])
    alcohol_drinking = st.selectbox('AlcoholDrinking', ['No', 'Yes'])
    stroke = st.selectbox('Stroke', ['No', 'Yes'])
    diff_walking = st.selectbox('DiffWalking', ['Yes', 'No'])
    sex = st.selectbox('Sex', ['Female', 'Male'])
    age_category = st.selectbox('AgeCategory', ['65-69', '80 or older', '60-64', '70-74', '75-79',
                                                '30-34', '18-24', '35-39', '25-29', '40-44', '55-59', 
                                                '50-54', '45-49'])
    diabetic = st.selectbox('Diabetic', ['Yes', 'No', 'No, borderline diabetes', 'Yes (during pregnancy)'])
    physical_activity = st.selectbox('PhysicalActivity', ['No', 'Yes'])
    asthma = st.selectbox('Asthma', ['No', 'Yes'])
    kidney_disease = st.selectbox('KidneyDisease', ['No', 'Yes'])

 
    input_data = CustomInputHeart(
    BMI=bmi,
    Smoking=smoking,
    AlcoholDrinking=alcohol_drinking,
    Stroke=stroke,
    DiffWalking=diff_walking,
    Sex=sex,
    AgeCategory=age_category,
    Diabetic=diabetic,
    PhysicalActivity=physical_activity,
    SleepTime=sleep_time,
    Asthma=asthma,
    KidneyDisease=kidney_disease
    )
    input_df = input_data.get_df()
    # Predict button
    if st.button('Predict'):

        pred = PredictionHeart()
        output = pred.predict(input_df)

        if output == "Yes":
            st.warning("You Have Heart Disease Please Consult A Docture",icon="🚨")
        else:
            st.warning("Your Don't Have Heart Disease Take care!")
        




# Predict Symptoms Page
if st.session_state.predict_symptoms:


    # list of symptoms
    symptoms = [
        'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 
        'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 
        'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 
        'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 
        'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 
        'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 
        'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 
        'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 
        'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 
        'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 
        'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 
        'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 
        'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 
        'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 
        'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 
        'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 
        'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 
        'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 
        'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 
        'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 
        'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 
        'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 
        'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 
        'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 
        'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 
        'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 
        'altered_sensorium', 'red_spots_over_body', 'belly_pain', 
        'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 
        'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 
        'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 
        'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 
        'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 
        'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 
        'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 
        'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 
        'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze', 
        'prognosis'
    ]
    # Initialize session state for managing button clicks and state
    if 'selected_symptoms' not in st.session_state:
        st.session_state.selected_symptoms = []

    if 'disease_predicted' not in st.session_state:
        st.session_state.disease_predicted = None

    # Initialize session state for managing button clicks
    if 'predict_diseases' not in st.session_state:
        st.session_state.predict_diseases = False
    if 'desc_button_clicked' not in st.session_state:
        st.session_state.desc_button_clicked = False

    if 'med_button_clicked' not in st.session_state:
        st.session_state.med_button_clicked = False

    if 'diet_button_clicked' not in st.session_state:
        st.session_state.diet_button_clicked = False
    
    # Create a multi-select dropdown
    selected_symptoms = st.multiselect('Select your symptoms:', symptoms)
    button = st.button("Predict")

   
        

    if button:
        

        if(len(selected_symptoms)==0):
            st.warning("Please provide you symptoms")
        #provide the input to the predict function and get the name of the diseases
        else:
            pred = prediction()
            #diseases = pred.predict(selected_symptoms)
            #st.warning(diseases)
            st.session_state.selected_symptoms = selected_symptoms
            st.session_state.disease_predicted = pred.predict(selected_symptoms)
            st.warning(f"Predicted Disease: {st.session_state.disease_predicted}")
            
    if st.session_state.disease_predicted:
        st.header("Recommendations")
        #send the diseases fro recommdation
        recommend = recommendation()
        description,medication,diets,precautaion,workout = recommend.recommendation_system(st.session_state.disease_predicted)


        # Display checkboxes for different recommendations
        desc_button = st.button("Show Description")
        if desc_button:
            st.write(description )
        med_button = st.button("Show Medication")
        if med_button:
            #st.write(medication)
            # Create a string to display the items with numbers
            items_str = "\n".join([f"{i+1}. {item}" for i, item in enumerate(medication)])

            # Display the items in a box
            st.text_area("Medication", items_str, height=150, max_chars=None)
            st.warning("Please Consult A Doctor Before Using It",icon= "🚨")

        diet_button = st.button("Show Diets")
        if diet_button:
            items_str = "\n".join([f"{i+1}. {item}" for i, item in enumerate(diets)])

            # Display the items in a box
            st.text_area("Diets", items_str, height=150, max_chars=None)
        pre_button = st.button("Precautions")
        if pre_button:
            items_str = "\n".join([f"{i+1}. {item}" for i, item in enumerate(precautaion)])

            # Display the items in a box
            st.text_area("Precaution", items_str, height=150, max_chars=None)
        work_button = st.button("Workouts Plans")
        if work_button:
            items_str = "\n".join([f"{i+1}. {item}" for i, item in enumerate(workout)])

            # Display the items in a box
            st.text_area("Workout", items_str, height=150, max_chars=None)


           