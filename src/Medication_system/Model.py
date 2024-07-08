import pandas as pd
import numpy as np
import sys
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from src.utils import save_obj
from src.logger import logging
from src.exception import CustomException


dataset = pd.read_csv('notebook\Health_data\Training.csv')
#notebook\Health_data\Training.csv
class ModelTraner:
    def __init__(self) -> None:
        pass
    def train_model(self):
        try:
            logging.info("Train test split")
            X = dataset.drop('prognosis', axis=1)
            y = dataset['prognosis']

            logging.info('do the lable encoding for the target columns')
            le = LabelEncoder()
            le.fit(y)
            y = le.transform(y)
            X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42  )

            logging.info("Building the modle")
            svc = SVC(kernel='linear')
            svc.fit(X_train,y_train)
            file_path = os.path.join('artifacts/Medication_models','medication.pkl')

            save_obj(file_path,svc)
            logging.info("Model saved")
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
    m = ModelTraner()
    m.train_model()