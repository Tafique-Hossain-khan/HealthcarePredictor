import pandas as pd
import numpy as np

from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
from sklearn.ensemble import AdaBoostClassifier
from src.utils import save_obj
from sklearn.model_selection import train_test_split
from sklearn.metrics import balanced_accuracy_score
import os,sys

@dataclass
class ModelTranerConfig:
    mode_trainer_path:str = os.path.join('artifacts','model.pkl')

class ModelTraner:
    def __init__(self) -> None:
        self.mode_traner = ModelTranerConfig()

    def initiate_model_traner(self,train_arr,test_arr):
        try:
            #split the data
            logging.info('spliting the traning dataset')
            X = train_arr[:, :-1]  
            y = train_arr[:, -1]

            #Model buliding
            X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
            
            
            ad = AdaBoostClassifier()
            ad.fit(X_train,y_train)
            y_pred = ad.predict(X_test)
            score = balanced_accuracy_score(y_test,y_pred)
            logging.info(f'Accuracy Score :{score}')

            save_obj(
                file_path=self.mode_traner.mode_trainer_path,
                obj= ad
            )



        except Exception as e:
            raise CustomException(e,sys)


