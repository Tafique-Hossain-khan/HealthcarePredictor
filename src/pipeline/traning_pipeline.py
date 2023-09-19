from src.components.data_transformation import DataTransformation
from src.components.data_injection import DataInjection
from src.logger import logging
import os,sys
from src.exception import CustomException
from src.components.model_traner import ModelTraner


if __name__ == "__main__":
    
    try:
        obj = DataInjection()
        train_data,test_data=obj.initiate_data_injection()
        print(train_data,test_data)
        preprocessor_obj = DataTransformation()
        train_arr,test_arr= preprocessor_obj.initiate_data_transformation(train_data,test_data)


        model_traner = ModelTraner()
        model_traner.initiate_model_traner(train_arr,test_arr)
    except Exception as e:
        raise CustomException(e,sys)