import streamlit as st

from src.Diabetes.pipeline.prediction_pipeline import CustomInput, Prediction
from src.Medication_system.recommend import prediction,recommendation


# Initialize session state variables
if 'diabetes' not in st.session_state:
    st.session_state.diabetes = False
if 'heart' not in st.session_state:
    st.session_state.heart = False
if 'predict_symptoms' not in st.session_state:
    st.session_state.predict_symptoms = False
if 'show_welcome' not in st.session_state:
    st.session_state.show_welcome = True  # Initialize welcome message state
# Sidebar components
st.sidebar.title("Medical app")
st.sidebar.image('https://cdn-icons-png.flaticon.com/512/124/124945.png')

diabetes_button = st.sidebar.button('Diabetes')
heart_button = st.sidebar.button('Heart')
symptoms_button = st.sidebar.button('Predict Symptoms')

# Update session state based on button clicks
if diabetes_button or heart_button or symptoms_button:
    st.session_state.show_welcome = False  # Hide welcome message on any button click

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


           