import os,sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from src.utils import load_object

class PredictionHeart:
    def __init__(self) -> None:
        pass

    def predict(self,features):

        try:
            
            preprocessor_path = os.path.join('artifacts/Heart_models','heart_preprocessor.pkl')
            
            model_path = os.path.join('artifacts/Heart_models','Heart_model.pkl')
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

class CustomInputHeart:
    def __init__(self,
                 BMI: float, Smoking: str, AlcoholDrinking: str, Stroke: str, 
                 DiffWalking: str, Sex: str, AgeCategory: str, Diabetic: str,
                 PhysicalActivity: str, SleepTime: int, Asthma: str, KidneyDisease: str) -> None:
        
        self.BMI = BMI
        self.Smoking = Smoking
        self.AlcoholDrinking = AlcoholDrinking
        self.Stroke = Stroke
        self.DiffWalking = DiffWalking
        self.Sex = Sex
        self.AgeCategory = AgeCategory
        self.Diabetic = Diabetic
        self.PhysicalActivity = PhysicalActivity
        self.SleepTime = SleepTime
        self.Asthma = Asthma
        self.KidneyDisease = KidneyDisease

    def get_df(self):
        logging.info("Creating the dataframe")
        try:
            data = {
                'BMI': [self.BMI],
                'Smoking': [self.Smoking],
                'AlcoholDrinking': [self.AlcoholDrinking],
                'Stroke': [self.Stroke],
                'DiffWalking': [self.DiffWalking],
                'Sex': [self.Sex],
                'AgeCategory': [self.AgeCategory],
                'Diabetic': [self.Diabetic],
                'PhysicalActivity': [self.PhysicalActivity],
                'SleepTime': [self.SleepTime],
                'Asthma': [self.Asthma],
                'KidneyDisease': [self.KidneyDisease]
            }

            logging.info(pd.DataFrame(data))
            return pd.DataFrame(data)
        except Exception as e:
            raise CustomException(e, sys)