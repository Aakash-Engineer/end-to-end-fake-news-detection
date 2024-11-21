from FakeNewsDetection.components.data_preprocessing import DataPreprocessing
from FakeNewsDetection import logger
from FakeNewsDetection.config.configuration import ConfigurationManager



STAGE_NAME = "Data Preprocessing"

def run_data_preprocessing_pipeline():
    try:
        logger.info(f'###############################   {STAGE_NAME}  ###############################\n')
        config_manager = ConfigurationManager()
        data_prepro_config = config_manager.get_data_preproconfig()
        data_preprocessing = DataPreprocessing(data_prepro_config)
        data_preprocessing.preprocess_data()
        logger.info(f'\n###############################  {STAGE_NAME} COMPLETED  ######################\n')
    except Exception as e:
        logger.error(f'Failed to execute stage: {STAGE_NAME}')
        logger.error(str(e))
        raise Exception(f'Failed to execute stage: {STAGE_NAME}') from e
    

if __name__ == '__main__':
    run_data_preprocessing_pipeline()