from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.pipeline.training_pipeline import TrainPipeline

if __name__ == '__main__':
    # mongodb_client = MongoDBClient()

    # print("Collection names:",mongodb_client.database.list_collection_names())

    train_pipeline = TrainPipeline()
    train_pipeline.run_pipeline()

   