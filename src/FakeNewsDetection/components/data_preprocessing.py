import os
from FakeNewsDetection import logger
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from FakeNewsDetection.entity.config_entity import PreprocessingConfig
from FakeNewsDetection.utils import stemming


class DataPreprocessing:
    def __init__(self, config: PreprocessingConfig):
        self.config = config
    
    def preprocess_data(self):
        try:
            df = pd.read_csv(self.config.raw_data_path)
            logger.info(f"Data read successfully from {self.config.raw_data_path}")
            
            # drop duplicates
            df.drop_duplicates(inplace=True)
            logger.info("Duplicates dropped")

            # drop rows with missing values
            df.dropna(subset=['title', 'text'], inplace=True, axis=0)
            logger.info("Rows with missing values dropped")

            # merge title and text columns
            df['text'] = df['title'] + ' ' + df['text']

            # drop other columns except title and label
            df.drop(columns=['title', 'subject', 'date'], inplace=True)
            logger.info("Columns dropped")

            # keep only alphabets and numbers
            df['text'] = df['text'].str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
            df['text'] = df['text'].str.lower()

            # perform stemming
            df['text'] = df['text'].apply(stemming)  
            logger.info("Stemming done")

            X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.05, random_state=1337)
            logger.info("Train test split done")
            # save train and test data
            train_data = pd.concat([X_train, y_train], axis=1)
            test_data = pd.concat([X_test, y_test], axis=1)

            train_data.to_csv(self.config.train_data_path, index=False)
            test_data.to_csv(self.config.test_data_path, index=False)
            logger.info("Train and test data saved")
            
        except Exception as e:
            logger.error(f"Data preprocessing failed: {e}")
            raise e
        



            