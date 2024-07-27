from dataclasses import dataclass
import os,sys
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier 
from sklearn.metrics import accuracy_score,balanced_accuracy_score
from src.logger import logging
from src.exception import CustomException
from src.utils import save_obj
@dataclass 
class ModelTranerConfig:
    model_trainer_config_path:str = os.path.join('artifacts/Diabetes_models','diabestes_model.pkl') 


class ModelTrainer:
    def __init__(self) -> None:
        self.mode_traner = ModelTranerConfig()


    def initiate_model_traner(self,X_train,X_test,y_train,y_test):
        try:
        
            ad = AdaBoostClassifier()
            ad.fit(X_train,y_train)
            y_pred = ad.predict(X_test)
            score = balanced_accuracy_score(y_test,y_pred)
            logging.info(f'Accuracy Score :{score}')

            save_obj(
                file_path=self.mode_traner.model_trainer_config_path,
                obj= ad
            )



        except Exception as e:
            raise CustomException(e,sys)