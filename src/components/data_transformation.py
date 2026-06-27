# main purpose of data transformation is to do feature engineering, selection, transformation
import os
import pickle
import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer #columntransformer is used to create a pipeline 
from sklearn.impute import SimpleImputer #used to handle the missing values in dataset
from sklearn.pipeline import Pipeline #used for pipeline define
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.components.data_ingestion import DataIngestionConfig
from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join("artifacts", "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        self.data_config = DataIngestionConfig()

    def get_data_transformer_object(self,data_path):
        try:
            logging.info("Loading raw data file in data transformer")

            data_path = None
            for candidate_path in [self.data_config.raw_data_path, self.data_config.train_data_path]:
                if os.path.exists(candidate_path):
                    data_path = candidate_path
                    break

            if data_path is None:
                project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
                data_path = os.path.join(project_root, "src", "stud.csv")

            df = pd.read_csv(data_path)
            logging.info("Loaded raw data file in data transformer")

            numerical_columns = df.select_dtypes(include=[np.number]).columns.to_list()
            categorical_columns = df.select_dtypes(include=['object']).columns.to_list()

            numerical_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                ]
            )

            logging.info(f"Numerical Pipeline initailized successfully\n{numerical_columns}")

            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("onehot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler())
                ]
            )
            
            logging.info(f"Categorical Pipeline initailized successfully:\n{categorical_columns}")

            preprocessor = ColumnTransformer(
                [
                    ("numerical_pipeline",numerical_pipeline,numerical_columns),
                    ("categorical_pipeline",categorical_pipeline,categorical_columns)
                ]
            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
    
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info("Train_df and Test_df are loaded!")
            logging.info("Initailizing Preprocessing object")
            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "math_score"
            #23:14 in video

        except Exception as e:
            CustomException(e,sys)