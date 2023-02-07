from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.exception import SensorException
from sensor.logger import logging
import sys
if __name__ == '__main__':
    # mongodb_client = MongoDBClient()

    # print("Collection names:",mongodb_client.database.list_collection_names())
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)
        
   