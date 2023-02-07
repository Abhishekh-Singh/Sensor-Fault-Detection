from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import DataValidationConfig
from sensor.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from sensor.utils.main_utils import read_yaml_file,write_yaml_file
from sensor.constant.training_pipeline import SCHEMA_FILE_PATH
import sys,os
from pandas import DataFrame
import pandas as pd
from scipy.stats import ks_2samp



'''
The validation concept here validates the pipeline and acts accordingly. 
It raises an exception if it fails to validate number of columns and if all numerical columns are not present
but it lets the pipeline run normally even if any drift is found in the dataset. 


'''

class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,
                    data_validation_config:DataValidationConfig):

        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(file_path=SCHEMA_FILE_PATH)
        except Exception as e:
            raise SensorException(e,sys)
                 
    def validate_number_of_columns(self,dataframe:DataFrame)-> bool:
        try:
            status = len(dataframe.columns) == len(self._schema_config['columns'])
            logging.info(f"Is required columns present in dataframe:[{status}]")
            logging.info(f"Required number of columns: {len(self._schema_config['columns'])}")
            logging.info(f"Dataframe has columns: {len(dataframe.columns)}")
            return status
        except Exception as e:
            raise SensorException(e,sys)
        # end try
    def is_numerical_column_exist(self,dataframe: DataFrame)-> bool:
        """
        This function check numerical column is present in dataframe or not
        :param df:
        :return: True if all column presents else False
        """
        try:
            
            dataframe_columns = dataframe.columns
            numerical_column_present = True
            missing_numerical_columns = []

            for column in self._schema_config["numerical_columns"]:
                if column not in dataframe_columns:
                    numerical_column_present = False
                    missing_numerical_columns.append(column)

            logging.info(f"Missing numerical columns: [{missing_numerical_columns}")  
            return numerical_column_present      

        except Exception as e:
            raise SensorException(e,sys)
        
    @staticmethod
    def read_data(file_path) -> DataFrame:
        try:
            return pd.read_csv(file_path)
              
        except Exception as e:
            raise SensorException(e,sys)

    def detect_dataset_drift(self,base_df,current_df,threshold=0.05)->bool:
        try:
            status = True
            report = {}
            for column in base_df.columns:
                d1 = base_df[column]
                d2 = current_df[column]
                is_same_dist = ks_2samp(d1,d2)
                if threshold<=is_same_dist.pvalue:
                    is_found = False
                else:
                    is_found= True
                    status = False
                report.update({column:{
                    "p_value": float(is_same_dist.pvalue),
                    "drift_status": is_found

                }})   
            #dumping
            drift_report_file_path = self.data_validation_config.drift_report_file_path
            #create directory
            dir_path = os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path,exist_ok=True)
            write_yaml_file(file_path=drift_report_file_path,content=report,replace=True)

            return status
        
        except Exception as e:
            raise SensorException(e,sys)
        # end try
        


    def initiate_data_validation(self)->DataValidationArtifact:
        """
        Method Name :   initiate_data_validation
        Description :   This method initiates the data validation component for the pipeline
        
        Output      :   Returns bool value based on validation results
        On Failure  :   Write an exception log and then raise an exception
           
        """
        try:
            error_message = ""
            logging.info("Starting data validation")
            train_dataframe = DataValidation.read_data(file_path = self.data_ingestion_artifact.trained_file_path)
            test_dataframe = DataValidation.read_data(file_path = self.data_ingestion_artifact.test_file_path)

            #validating no of columns
            #training data
            status = self.validate_number_of_columns(dataframe=train_dataframe)
            logging.info(f"All required columns present in training dataframe: {status}")
            if not status:
                error_message += f"Columns are missing in training dataframe.\n"

            #test data
            status = self.validate_number_of_columns(dataframe=test_dataframe)
            logging.info(f"All required columns present in test dataframe: {status}")
            if not status:
                error_message += f"Columns are missing in test dataframe.\n"    


            #Validate Numerical columns
            status = self.is_numerical_column_exist(dataframe=train_dataframe)
            logging.info(f"All required columns present in training dataframe: {status}")
            if not status:
                error_message += f"Numerical Columns are missing in training dataframe.\n"

            #test data
            status = self.is_numerical_column_exist(dataframe=test_dataframe)
            logging.info(f"All required columns present in test dataframe: {status}")
            if not status:
                error_message += f"Numerical Columns are missing in test dataframe.\n"

            if len(error_message) > 0:
                raise Exception(error_message)


            #checking data drift

            status = self.detect_dataset_drift(base_df=train_dataframe,current_df=test_dataframe)

            data_validation_artifact = DataValidationArtifact(
                        validation_status = status,
                        valid_train_file_path = self.data_ingestion_artifact.trained_file_path,
                        valid_test_file_path = self.data_ingestion_artifact.test_file_path,
                        invalid_train_file_path = None,
                        invalid_test_file_path = None,
                        drift_report_file_path = self.data_validation_config.drift_report_file_path
            )
            logging.info(f"Data validation artifact: {data_validation_artifact}")

           
        except Exception as e:
            raise SensorException(e,sys)
       
