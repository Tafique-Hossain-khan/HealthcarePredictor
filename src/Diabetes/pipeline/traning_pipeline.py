from dataclasses import dataclass
import pandas as pd
from src.logger import logging
import os,sys
from src.exception import CustomException

from src.Diabetes.components.preprocessing import PreProcessing
from src.Diabetes.components.model_traner import ModelTrainer

if __name__ == "__main__":
    try:
        # Load the dataset
        df = pd.read_csv('notebook/data/diabetes_prediction_dataset.csv')
        
        # Create an instance of PreProcessing
        preprocessor = PreProcessing()
        
        # Call the initiate_data_transformation method
        X_train,X_test,y_train,y_test = preprocessor.initiate_data_transformation(df=df)
        
        # Create an instance of ModelTrainer
        model_trainer = ModelTrainer()
        logging.info("Model trainer initiated")
        
        # Call the initiate_model_trainer method
        model_trainer.initiate_model_traner( X_train,X_test,y_train,y_test )
    
    except Exception as e:
        raise CustomException(e, sys)