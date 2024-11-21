from FakeNewsDetection.constants import *
from FakeNewsDetection.utils.common import read_yaml, create_directories
from FakeNewsDetection.entity.config_entity import DataIngestionConfig, DataValidationConfig, PreprocessingConfig, TrainingConfig

class ConfigurationManager:
    def __init__(self, 
                 config_path= CONFIG_FILE,
                 parama_path= PARAMS_FILE,
                 schema_path= SCHEMA_FILE):
        
        self.config = read_yaml(config_path)
        self.params = read_yaml(parama_path)
        self.schema = read_yaml(schema_path)

        create_directories([self.config.artifact_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
    def get_datavalidation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])

        return DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_path=config.unzip_data_path,
            status_file_path=config.status_file_path,
            all_schema=self.schema.COLUMNS
        )
    
    def get_data_preproconfig(self):
        config = self.config.data_preprocessing
        create_directories([config.root_dir])

        return PreprocessingConfig(
            root_dir= Path(config.root_dir),
            raw_data_path= Path(config.raw_data_path),
            train_data_path= Path(config.train_data_path),
            test_data_path= Path(config.test_data_path),
            status_file_path= Path(config.status_file_path)
        )
    def get_training_config(self) -> TrainingConfig:
        config = self.config.training
        create_directories([config.root_dir])

        return TrainingConfig(
            root_dir = Path(config.root_dir),
            train_data_path = Path(config.train_data_path),
            model_path = Path(config.model_path)
        )
