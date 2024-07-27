import pandas as pd
import os,sys
from dataclasses import dataclass
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.model_selection import train_test_split
from src.exception import CustomException
from src.logger import logging
from imblearn.over_sampling import SMOTE
from src.utils import save_obj,get_balance_dataset
from imblearn.under_sampling import RandomUnderSampler


@dataclass
class preprocessorCofig:
    preprocessor_path_config:str = os.path.join('artifacts/Heart_models','heart_preprocessor.pkl')

class PreProcessing:
    def __init__(self) -> None:
        self.preprocessor_path = preprocessorCofig()

    def get_data_transformed_obj(self,df):

        try:
            logging.info(df.columns)
            logging.info("data transformation started")
            
            df = df.drop(columns=['HeartDisease'],axis='columns')
            #seperate the numercial and categorical col
            num_col = df.select_dtypes(include=['int','float']).columns
            cat_col = df.select_dtypes(include=['object']).columns


            
            logging.info("Pipeline")
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', 'passthrough', num_col),  # Pass through numerical columns unchanged
                    ('cat', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'), cat_col),  # Apply OHE to categorical columns
                
                ],
                remainder='passthrough'  # Drop any columns not specified in transformers
            )
            
            logging.info("preprocessing completed")
            return preprocessor 
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,df):
        ##do train test split
        try:
            #remove duplicates
            df = df.drop_duplicates()
            #remove unnecessary col
            df.drop(columns=[#'HeartDisease', 'BMI', 'Smoking', 'AlcoholDrinking', 'Stroke',
            'PhysicalHealth', 
                        'MentalHealth',#  'DiffWalking', 'Sex', 'AgeCategory',
            'Race',
            #  'Diabetic', 'PhysicalActivity', 
                'GenHealth',
                #'SleepTime',#'Asthma', 'KidneyDisease', 
            'SkinCancer'
            ],inplace=True,axis=1)

            logging.info('Initaating data transformation')
            preprocessor_obj = self.get_data_transformed_obj(df)

            
            
            logging.info(df)
            #Down sampleing
            X = df.drop(columns=['HeartDisease'],axis='columns')
            y = df['HeartDisease']
            logging.info(X.columns)
            rus = RandomUnderSampler(random_state=42)
            X_res,y_res = rus.fit_resample(X,y) 
            logging.info(X_res.head(1))
            logging.info(X_res.columns)
            X_res.reset_index(drop=['index'],inplace=True)
            y_res.reset_index(drop=['index'],inplace=True)
            
        
            X_train,X_test,y_train,y_test = train_test_split(X_res,y_res,test_size=0.2,random_state=42)
            logging.info(X_train.columns)
            logging.info(X_res.columns)
            logging.info("Transformation started")
            X_train_transformed = preprocessor_obj.fit_transform(X_train)
            X_test_transformed = preprocessor_obj.transform(X_test)
            logging.info("Saving the model")
            save_obj(file_path=self.preprocessor_path.preprocessor_path_config,obj=preprocessor_obj)
            #X_train,X_test,y_train,y_test = train_test_split(X_resampled,y_resampled,test_size=0.2,random_state=42)
            logging.info("prprocessor obj completed")
            
            return X_train_transformed,X_test_transformed,y_train,y_test
        
        except Exception as e:
            raise CustomException(e,sys)
        
'''
if __name__=="__main__":
    # Load the dataset
        df = pd.read_csv('notebook\data\heart_2020_cleaned.csv')
        
        # Create an instance of PreProcessing
        preprocessor = PreProcessing()
        preprocessor.initiate_data_transformation(df)
'''