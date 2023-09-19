import os,sys
from src.exception import CustomException
from src.logger import logging

import pickle
import numpy as np
import pandas as pd
#for balencing the dataset
from imblearn.under_sampling import RandomUnderSampler
from collections import Counter

def load_object(file_path):

    with open(file_path,'wb') as f:
        pickle.loads(f)

def save_obj(file_path,obj):

    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)

        with open(file_path,'wb') as f:
            pickle.dump(obj,f)

    except Exception as e:
        raise CustomException(e,sys)
    
    
# Appying RandomUndersampeling to unbalance dataset
def get_balance_dataset(df):
   
    try:
        
        logging.info('spliting the traning dataset')
        X = df.iloc[:, :-1]  
        y = df.iloc[:, -1]   

        rs = RandomUnderSampler()
        X_res,y_res = rs.fit_resample(X,y) 
        logging.info(f'Balance dataset value:{Counter(y_res)}')

        final_resample_df = np.c_[X_res,y_res]

        return(
            final_resample_df
        )

    except Exception as e:
        raise CustomException(e,sys)

'''
if __name__ == "__main__":
    obj = DataInjection()
    train_arr,test_arr = obj.initiate_data_injection()
    pre_obj = DataTransformation()
    train_df,test_df = pre_obj.initiate_data_transformation(train_arr,test_arr)
    logging.info(train_df)

    get_balance_dataset(pd.DataFrame(train_df))
    '''
    

