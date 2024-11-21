import os
import urllib.request as request
import zipfile
from FakeNewsDetection import logger
import gdown
from FakeNewsDetection.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    # function to download data from google drive
    
    def download_data(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                logger.info("Downloading data from source")
                # download data from google drive
                gdown.download(self.config.source_url, self.config.local_data_file, quiet=False)
                logger.info("Data downloaded successfully")
            else:
                logger.info("Data already exists")
        except Exception as e:
            logger.error(f"Error downloading data: {e}")
            raise e
    def unzip_data(self):
        try:
            if os.path.exists(self.config.local_data_file):
                with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                    zip_ref.extractall(self.config.unzip_dir)
                logger.info("Data unzipped successfully")
            else:
                logger.info("Data already unzipped")
        except Exception as e:
            logger.error(f"Error unzipping data: {e}")
            raise e
