# from Insurance_Premium.config import mongo_client
from config import mongo_client
import pandas as pd 
# from Insurance_Premium.logger import logging
from logger import logging
# from Insurance_Premium.exception import InsuranceException
from exception import InsuranceException
import os,sys
import yaml
import dill
import numpy as np


def get_collection_as_dataframe(database_name:str, collection_name:str)->pd.DataFrame:
    try : 
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id ")
        df = df.drop("_id",axis=1)
        logging.info(f"Row and columns in df: {df.shape}")
        return df
    except Exception as ex:
        raise InsuranceException(ex, sys)


def write_yaml_file(file_path,data:dict):
    try:
        file_dir = os.path.dirname(file_path)
        os.makedirs(file_dir,exist_ok=True)
        with open(file_path,"w") as file_writer:
            yaml.dump(data,file_writer)
    except Exception as ex:
        raise InsuranceException(ex, sys)

def load_object(file_path: str, ) -> object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file: {file_path} is not exists")
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    except Exception as ex:
        raise InsuranceException(ex, sys) from ex


def save_numpy_array_data(file_path: str, array: np.array):

    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as ex:
        raise InsuranceException(ex, sys) from ex