import os
from FakeNewsDetection import logger
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.feature_extraction.text import TfidfVectorizer
import json
from FakeNewsDetection.entity.config_entity import EvaluationConfig



class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    def evaluate(self):
        try:
            # load model
            model = joblib.load(self.config.model_path)
            logger.info('Model loaded successfully')

            # load vectorizer
            vectorizer = joblib.load(self.config.vectorizer_path)
            # load test data
            test_data = pd.read_csv(self.config.test_data_path)
            logger.info('Test data loaded successfully')

            # vectorize data
            X = vectorizer.transform(test_data['text']).toarray()
            y = test_data['label']
            logger.info('Data vectorized successfully')
            # free memory
            del test_data

            # predict
            y_pred = model.predict(X)
            # calculate metrics
            accuracy = accuracy_score(y, y_pred)
            precision = precision_score(y, y_pred)
            recall = recall_score(y, y_pred)
            f1 = f1_score(y, y_pred)
            logger.info('Metrics calculated successfully')

            # save metrics in evaluation_metrics_path in json fromat
            metrics = {
                'accuracy': accuracy,
                'precision': precision,
                'recall': recall,
                'f1': f1
            }
            # log metrics
            logger.info(f'Accuracy: {accuracy}')
            logger.info(f'Precision: {precision}')
            logger.info(f'Recall: {recall}')
            logger.info(f'F1: {f1}')
            with open(self.config.evaluation_metrics_path, 'w') as f:
                json.dump(metrics, f)
            logger.info('Metrics saved successfully')

        except Exception as e:
            logger.error(f'Error in evaluation: {e}')
            raise e

