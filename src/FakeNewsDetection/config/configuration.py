from FakeNewsDetection.constants import *
from FakeNewsDetection.utils.common import read_yaml, create_directory
from FakeNewsDetection.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self, 
                 config_path= CONFIG_FILE,
                 parama_path= PARAMS_FILE):
        
        self.config = read_yaml(config_path)
        self.params = read_yaml(parama_path)

        create_directory([self.config.artifact_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directory([config.root_dir])

        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
