from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import os,sys

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

from src.utils import save_obj
from src.components.data_injection import DataInjection

@dataclass 
class DataTransformationConfig:
    preprocessor_path_config:str = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self) -> None:
        self.preprocessor_path = DataTransformationConfig()

    def get_data_transformed_obj(self,df):
        
       
        try:
            cat_col = df.select_dtypes(include=object)
            cat_col = list(cat_col)
            cat_pipeline = Pipeline([
                ('ohe',OneHotEncoder(drop='first'))
            ])
            preprocessor = ColumnTransformer([
                ('cat',cat_pipeline,cat_col)
            ],remainder='passthrough')
            
            return preprocessor 
        except Exception as e:
            raise CustomException(e,sys)
        

    def initiate_data_transformation(self,train_data_path,test_data_path):

        try:
            logging.info('Reading the dataset')
            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)

            logging.info('Crating the preprocessor obj')
            preprocessor_obj = self.get_data_transformed_obj(train_df)
            target_col = ['diabetes']

            # for train set
            logging.info('spliting the traning dataset')
            input_feature_train_df = train_df.drop(target_col,axis=1)
            target_feature_train_df = train_df[target_col]

            # for test set
            logging.info('Spliting the testing dataset')
            input_feature_test_df = test_df.drop(target_col,axis=1)
            target_feature_test_df = test_df[target_col]

            input_feater_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feater_test_arr = preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feater_train_arr,np.array(target_feature_train_df)]
            test_arr = np.c_[input_feater_test_arr,np.array(target_feature_test_df)]
            logging.info('Saving the preprocessor obj in artifacts')
           
            save_obj(file_path=self.preprocessor_path.preprocessor_path_config,obj= preprocessor_obj)
            return(
                train_arr,
                test_arr
            )


        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataInjection()
    train_arr,test_arr = obj.initiate_data_injection()

    pre_obj = DataTransformation()
    pre_obj.initiate_data_transformation(train_arr,test_arr)