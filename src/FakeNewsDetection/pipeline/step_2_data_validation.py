from FakeNewsDetection.components.data_validation import DataValidation
from FakeNewsDetection.config.configuration import ConfigurationManager
from FakeNewsDetection import logger



STAGE_NAME = 'Data Validation'

def run_data_validation_pipeline():
    try:
        logger.info(f"\n###############################   {STAGE_NAME}  ###############################\n")
        config_manager = ConfigurationManager()
        data_validation_config = config_manager.get_datavalidation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_data_columns()
        logger.info(f"\n###############################  {STAGE_NAME} COMPLETED  ######################\n")
    except Exception as e:
        logger.error(f"Failed to execute stage: {STAGE_NAME}")
        logger.error(str(e))
        raise Exception(f"Failed to execute stage: {STAGE_NAME}") from e
    


if __name__ == '__main__':
    run_data_validation_pipeline()