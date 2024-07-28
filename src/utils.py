import os,sys
from src.exception import CustomException
from src.logger import logging

import pickle
import numpy as np
import pandas as pd

from collections import Counter


def load_object(file_path):
    try:
        with open(file_path, 'rb') as f:
            obj = pickle.load(f)
        return obj
    except Exception as e:
        raise CustomException(e, sys)


def save_obj(file_path,obj):

    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)

        with open(file_path,'wb') as f:
            pickle.dump(obj,f)

    except Exception as e:
        raise CustomException(e,sys)
    
    

