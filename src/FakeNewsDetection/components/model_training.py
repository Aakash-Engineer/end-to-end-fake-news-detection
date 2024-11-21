import os
from FakeNewsDetection import logger
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
from FakeNewsDetection.entity.config_entity import TrainingConfig
import joblib

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    def train(self):
        try:
            # load training data
            train_data = pd.read_csv(self.config.train_data_path)
            logger.info(f"Training data loaded from {self.config.train_data_path}")
            # vectorize it
            vectorizer = TfidfVectorizer(max_features=200, stop_words='english')
            X = vectorizer.fit_transform(train_data['text']).toarray()
            y = train_data['label'].values
            # remove train data from memory
            del train_data

            # save vectorizer
            joblib.dump(vectorizer, self.config.vectorizer_path)
            logger.info(f"Vectorizer saved at {self.config.vectorizer_path}")

            # create logidtic regression model
            model = LogisticRegression()
            model.fit(X, y)
            logger.info("Model trained successfully")
            # save model in pickle, path is in config
            joblib.dump(model, self.config.model_path)
            logger.info(f"Model saved at {self.config.model_path}")
        except Exception as e:
            logger.error(f"Training failed: {str(e)}")
            raise e