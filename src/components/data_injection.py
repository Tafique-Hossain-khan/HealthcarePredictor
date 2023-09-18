from src.exception import CustomException
from src.logger import logging
import os,sys
from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split


@dataclass
class DataInjectionConfig:
    raw_data_path:str = os.path.join('artifacts','raw_data.csv')
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')

class DataInjection:
    def __init__(self) -> None:
        self.data_path = DataInjectionConfig()

    def initiate_data_injection(self):
        try:
            logging.info('Data injection initiated')
            #read the data from the data source and save it to raw data 
            df = pd.read_csv('notebook\data\diabetes_prediction_dataset.csv')
            #create the directory 
            os.makedirs(os.path.dirname(self.data_path.raw_data_path),exist_ok=True)
            df.to_csv(self.data_path.raw_data_path,header=True,index=False)
            #split the data into train and test
            train_data,test_data = train_test_split(df,train_size=0.30,random_state=42)
            train_data.to_csv(self.data_path.train_data_path,header= True,index=False)
            test_data.to_csv(self.data_path.test_data_path,header= True,index=False)
            logging.info('Train Test complited')

            return(
                self.data_path.train_data_path,
                self.data_path.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataInjection()
    obj.initiate_data_injection()

