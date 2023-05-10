from sensor.exception import SensorException
from sensor.logger import logging
import yaml
import os,sys
import numpy as np
import dill

def read_yaml_file(file_path: str)-> dict:
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise SensorException(e,sys)
    # end try

def write_yaml_file(file_path: str,content: object, replace: bool = False)-> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
            os.makedirs(os.path.dirname(file_path),exist_ok=True)
            with open(file_path,'w') as file:
                yaml.dump(content,file)    
    except Exception as e:
        raise SensorException(e,sys)
    # end try

def save_numpy_array_data(file_path: str, array: np.array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path,'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise SensorException(e,sys) from e



   
def load_numpy_array_data(file_path: str)->np.array:
    try:
        with open(file_path,'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise SensorException(e,sys) from e
    # end try


def save_object(file_path: str, obj: object)-> None:
    try:
        logging.info("Entered the save_object method of MainUtils class")
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
        logging.info("Exited the save_object method of MainUtils class")

    except Exception as e:
        raise SensorException(e,sys) from e
    # end try
