import pandas as pd
import sys
import os
from src.utils import save_obj,load_object
from src.logger import logging
from src.exception import CustomException
import numpy as np
import json
desc = pd.read_csv('notebook/Health_data/description.csv')
med = pd.read_csv('notebook/Health_data/medications.csv')
diet = pd.read_csv('notebook/Health_data/diets.csv')
pre = pd.read_csv('notebook/Health_data/precautions_df.csv')
sym = pd.read_csv('notebook/Health_data/symtoms_df.csv')
workout = pd.read_csv('notebook/Health_data/workout_df.csv')
import ast
class prediction:

    def __init__(self) -> None:
        pass

    def predict(self,lst):
        try:
            logging.info("Load the modle")
            file_path = os.path.join('artifacts/Medication_models','medication.pkl')

            model= load_object(file_path)

            input_array = np.zeros(132)
            #make the input by replacing 1 in the input_array  where the given symptomes in the list
            diseases_list = {
            0: '(vertigo) Paroymsal  Positional Vertigo', 1: 'AIDS', 2: 'Acne', 3: 'Alcoholic hepatitis',
            4: 'Allergy', 5: 'Arthritis', 6: 'Bronchial Asthma', 7: 'Cervical spondylosis', 8: 'Chicken pox',
            9: 'Chronic cholestasis', 10: 'Common Cold', 11: 'Dengue', 12: 'Diabetes', 13: 'Dimorphic hemmorhoids(piles)',
            14: 'Drug Reaction', 15: 'Fungal infection', 16: 'GERD', 17: 'Gastroenteritis', 18: 'Heart attack',
            19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 23: 'Hypertension',
            24: 'Hyperthyroidism', 25: 'Hypoglycemia', 26: 'Hypothyroidism', 27: 'Impetigo', 28: 'Jaundice',
            29: 'Malaria', 30: 'Migraine', 31: 'Osteoarthristis', 32: 'Paralysis (brain hemorrhage)', 33: 'Peptic ulcer diseae',
            34: 'Pneumonia', 35: 'Psoriasis', 36: 'Tuberculosis', 37: 'Typhoid', 38: 'Urinary tract infection',
            39: 'Varicose veins', 40: 'hepatitis A'
            }

            with open('notebook/symp.json','r') as f:
                symp = json.load(f)

            for s in lst:
                input_array[symp[s]]=1
            #provide the input array for predicton

            prediction = model.predict([input_array])[0]
            diseases = diseases_list[prediction]

            return diseases

        except Exception as e:
            raise CustomException(e,sys)
        
class recommendation:
    def __init__(self) -> None:
        pass

    def recommendation_system(self,diseases):

        try:
            #get the discription fo the diseases
            description = desc[desc['Disease'] == diseases]['Description'].values
            description = " ".join([w for w in description])

            #medication
            ind_medication = med[med['Disease'] == diseases].index[0]
            medication = ast.literal_eval(med['Medication'][ind_medication])
            

            #diet
            ind_diets = diet[diet['Disease'] == diseases].index[0]
            diets = ast.literal_eval(diet['Diet'][ind_diets])

            #precaution
            ind_pre = pre[pre['Disease']==diseases].index[0]
            precautaion = pre[['Precaution_1'	,'Precaution_2'	,'Precaution_3'	,'Precaution_4']].iloc[ind_pre].values.tolist()

            #workout
            workout[workout['disease']==diseases]['workout'].values.tolist()

            return description,medication,diets,precautaion,workout
        except Exception as e:
            raise CustomException(e,sys)


