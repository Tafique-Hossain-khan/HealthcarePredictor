from flask import Flask, render_template, request, jsonify
from src.Heart.pipeline.prediction_pipeline import PredictionHeart,CustomInputHeart
from src.Diabetes.pipeline.prediction_pipeline import CustomInput, Prediction
from src.Medication_system.recommend import prediction,recommendation
import json

app = Flask(__name__)

# Add a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diabetes_predictor', methods=['GET', 'POST'])
def diabetes_predictor():
    prediction_text = None
    if request.method == 'POST':
        try:
            gender = request.form['gender']
            age = int(request.form['age'])
            hypertension = int(request.form['Hig_Blood_pressure'])
            heart_disease = 0
            smoking_history = request.form['smoking_history']
            bmi = float(request.form['bmi'])
            HbA1c_level = float(request.form['hemoglobin_a1c'])
            blood_glucose_level = int(request.form['blood_glucose_level'])

            obj = CustomInput(
                gender=gender,
                age=age,
                hypertension=hypertension,
                heart_disease=heart_disease,
                smoking_history=smoking_history,
                bmi=bmi,
                HbA1c_level=HbA1c_level,
                blood_glucose_level=blood_glucose_level
            )
            
            features = obj.get_df()
            predict_obj = Prediction()
            prediction = predict_obj.predict(features)

            if prediction == 1:
                prediction_text = "You have diabetes, please consult a doctor."
            else:
                prediction_text = "You don't have diabetes! Take care."
        except Exception as e:
            prediction_text = f"Error: {str(e)}"
    
    return render_template('diabetes.html', prediction=prediction_text)

@app.route('/heart_predictor', methods=['GET', 'POST'])
def heart_predictor():
    prediction_text = None
    if request.method == 'POST':
        try:
            # Get form data with validation and default values
            bmi = float(request.form.get('bmi', 25.0))
            sleep_time = float(request.form.get('sleeptime', 7.0))
            
            # Get these values directly without conversion
            smoking = request.form.get('smoking', 'No')
            alcohol_drinking = request.form.get('alcoholdrinking', 'No')
            stroke = request.form.get('stroke', 'No')
            diff_walking = request.form.get('diffWalking', 'Yes')
            sex = request.form.get('sex', 'Female')
            age_category = request.form.get('agecategory', '18-24')
            diabetic = request.form.get('diabetic', 'No')
            physical_activity = request.form.get('physicalactivity', 'No')
            asthma = request.form.get('asthma', 'No')
            kidney_disease = request.form.get('kidneydisease', 'No')

            # Create input object
            input_data = CustomInputHeart(
                BMI=bmi,
                Smoking=smoking,
                AlcoholDrinking=alcohol_drinking,
                Stroke=stroke,
                DiffWalking=diff_walking,
                Sex=sex,
                AgeCategory=age_category.strip(),
                Diabetic=diabetic,
                PhysicalActivity=physical_activity,
                SleepTime=sleep_time,
                Asthma=asthma,
                KidneyDisease=kidney_disease
            )
            
            input_df = input_data.get_df()
            pred = PredictionHeart()
            output = pred.predict(input_df)

            if output == "Yes":
                prediction_text = "You Have Heart Disease Please Consult A Doctor 🚨"
            else:
                prediction_text = "You Don't Have Heart Disease! Take care!"

        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return render_template('heart.html', error=f"An error occurred: {str(e)}")

    return render_template('heart.html', prediction=prediction_text)

@app.route('/symptoms_predictor', methods=['GET', 'POST'])
def symptoms_predictor():
    if request.method == 'POST':
        try:
            # Get selected symptoms from the form
            symptoms_json = request.form.get('symptoms[]')
            if not symptoms_json:
                return render_template('symptoms.html', error="Please select at least one symptom")
            
            selected_symptoms = json.loads(symptoms_json)
            print("Selected symptoms:", selected_symptoms)  # Debug print
            
            # Get prediction
            pred = prediction()
            disease_predicted = pred.predict(selected_symptoms)
            print("Predicted disease:", disease_predicted)  # Debug print
            
            # Get recommendations
            recommend = recommendation()
            description, medication, diets, precaution, workout = recommend.recommendation_system(disease_predicted)
            
            # Clean the data - handle both string and list cases
            def clean_data(data):
                if isinstance(data, str):
                    return data.strip("[]'").split("', '")
                elif isinstance(data, list):
                    return data
                return []

            # Clean all data
            description = clean_data(description)
            medication = clean_data(medication)
            diets = clean_data(diets)
            precaution = clean_data(precaution)
            workout = clean_data(workout)
            
            print("Recommendations loaded")  # Debug print
            
            return render_template('symptoms.html', 
                prediction={'disease': disease_predicted, 'description': description[0] if description else ""},
                recommendations={
                    'description': description[0] if description else "",
                    'medication': medication,
                    'diets': diets,
                    'precaution': precaution,
                    'workout': workout
                })
            
        except Exception as e:
            print(f"Error occurred: {str(e)}")  # Debug print
            return render_template('symptoms.html', error=str(e))
    
    return render_template('symptoms.html')

if __name__ == '__main__':
    app.debug = True
    app.run()