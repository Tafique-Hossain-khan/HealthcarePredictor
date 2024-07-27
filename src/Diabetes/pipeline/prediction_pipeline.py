import os,sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from src.utils import load_object

class Prediction:
    def __init__(self) -> None:
        pass

    def predict(self,features):

        try:
            
            preprocessor_path = os.path.join('artifacts/Diabetes_models','diabestes_preprocessor.pkl')
            
            model_path = os.path.join('artifacts/Diabetes_models','diabestes_model.pkl')
            logging.info("Path creation done")

            preprocessor = load_object(preprocessor_path)
            logging.info("preprocessor loaded")
            model = load_object(model_path)
            logging.info("model loaded")
            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            logging.info(f'The output is{pred}')
            
            return pred

        except Exception as e:
            raise CustomException(e,sys)



class CustomInput:
    def __init__(self,
                 	gender:str,	age:int,	hypertension:int,	heart_disease:int,	smoking_history:int,
                        	bmi:float,	HbA1c_level:float,	blood_glucose_level:int) -> None:
        
        self.gender = gender
        self.age = age
        self.hypertension = hypertension
        self.heart_disease = heart_disease
        self.smoking_history = smoking_history
        self.bmi = bmi
        self.HbA1c_level = HbA1c_level
        self.blood_glucose_level = blood_glucose_level

    

    def get_df(self):
            logging.info("Crating the dataframe")
            try:
                
                data = {
                'gender': [self.gender],
                'age': [self.age],
                'hypertension': [self.hypertension],
                'heart_disease': [self.heart_disease],
                'smoking_history': [self.smoking_history],
                'bmi': [self.bmi],
                'HbA1c_level': [self.HbA1c_level],
                'blood_glucose_level': [self.blood_glucose_level]
            }

                logging.info(pd.DataFrame(data))
                
                return pd.DataFrame(data)
            except Exception as e:
                raise CustomException(e,sys)
            


if __name__ == "__main__":
    
    ci = CustomInput('Female'	,80.0	,0	,1,	'never'	,25.19,	6.6	,140)
    df = ci.get_df()
    logging.info(df)

    pred_obj = Prediction()
    
    pred = pred_obj.predict(df)
    
