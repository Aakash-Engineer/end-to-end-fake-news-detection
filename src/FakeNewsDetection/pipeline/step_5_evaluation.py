from FakeNewsDetection.components.evaluation import Evaluation
from FakeNewsDetection.config.configuration import ConfigurationManager
from FakeNewsDetection import logger



STAGE_NAME = 'Evaluation'


def run_evaluation_pipeline():
    try:
        logger.info(f'###############################   {STAGE_NAME}  ###############################\n')
        config_manager = ConfigurationManager()
        evaluation_config = config_manager.get_evaluation_config()
        evaluation = Evaluation(evaluation_config)
        evaluation.evaluate()
        logger.info(f'\n###############################  {STAGE_NAME} COMPLETED  ######################\n')
    except Exception as e:
        logger.error(f'Failed to execute stage: {STAGE_NAME}')
        logger.error(str(e))
        raise Exception(f'Failed to execute stage: {STAGE_NAME}') from e
    

if __name__ == '__main__':  
    run_evaluation_pipeline()