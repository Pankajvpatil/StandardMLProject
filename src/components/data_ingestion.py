import os, sys
# lets add src folder to the path so that we can import the modules from src folder
# print(os.path.join(os.getcwd(), "src"))
# sys.path.append(os.path.join(os.getcwd(), "src"))
from src.exception import CustomException
from src.logger import logging
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


class DataIngestionConfig:
    def __init__(self):
        self.train_data_path = os.path.join('artifacts', 'train.csv')
        self.test_data_path = os.path.join('artifacts', 'test.csv')
        self.raw_data_path = os.path.join('artifacts', 'raw.csv')

    def initiate_data_ingestion(self, file_path):
        logging.info("Entered the data ingestion method or component")
        try:
            logging.info(f"Reading the dataset from {file_path}")
            df = pd.read_csv(file_path)
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.train_data_path), exist_ok=True)

            df.to_csv(self.raw_data_path, index=False, header=True)
            logging.info("Train test split initiated")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.train_data_path, index=False, header=True)
            test_set.to_csv(self.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.train_data_path,
                self.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)
        


if __name__ == "__main__":
    obj = DataIngestionConfig()
    train_data, test_data = obj.initiate_data_ingestion(file_path=os.path.join(os.getcwd(), 'notebooks\\data', 'StudentsPerformance.csv'))   
