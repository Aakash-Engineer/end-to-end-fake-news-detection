from FakeNewsDetection.components.data_ingestion import DataIngestion
from FakeNewsDetection.config.configuration import ConfigurationManager
from FakeNewsDetection import logger


STAGE_NAME = 'Data Ingestion'

def run_data_ingestion_pipeline():
    try:
        logger.info(f"\n###############################   {STAGE_NAME}  ###############################\n")
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.unzip_data()
        logger.info(f"\n###############################  {STAGE_NAME} COMPLETED  ######################\n")
    except Exception as e:
        logger.error(f"Failed to execute stage: {STAGE_NAME}")
        logger.error(str(e))
        raise Exception(f"Failed to execute stage: {STAGE_NAME}") from e
    
if __name__ == '__main__':
    run_data_ingestion_pipeline()