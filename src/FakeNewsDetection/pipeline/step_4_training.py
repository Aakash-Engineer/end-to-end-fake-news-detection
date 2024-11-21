from FakeNewsDetection.components.model_training import Training
from FakeNewsDetection import logger
from FakeNewsDetection.config.configuration import ConfigurationManager



STAGE_NAME = "Training"

def run_training_pipeline():
    try:
        logger.info(f'###############################   {STAGE_NAME}  ###############################\n')
        config_manager = ConfigurationManager()
        training_config = config_manager.get_training_config()
        training = Training(training_config)
        training.train()
        logger.info(f'\n###############################  {STAGE_NAME} COMPLETED  ######################\n')
    except Exception as e:
        logger.error(f'Failed to execute stage: {STAGE_NAME}')
        logger.error(str(e))
        raise Exception(f'Failed to execute stage: {STAGE_NAME}') from e
    


if __name__ == '__main__':
    run_training_pipeline()