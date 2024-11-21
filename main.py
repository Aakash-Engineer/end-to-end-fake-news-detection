from FakeNewsDetection.pipeline.step_1_data_ingestion import run_data_ingestion_pipeline
from FakeNewsDetection.pipeline.step_2_data_validation import run_data_validation_pipeline
from FakeNewsDetection.pipeline.step_3_data_preprocessing import run_data_preprocessing_pipeline
from FakeNewsDetection.pipeline.step_4_training import run_training_pipeline
from FakeNewsDetection.pipeline.step_5_evaluation import run_evaluation_pipeline

# run data ingestion pipeline
# run_data_ingestion_pipeline()

# run data validation pipeline
run_data_validation_pipeline()

# run data preprocessing pipeline
run_data_preprocessing_pipeline()

# run training pipeline
run_training_pipeline()

# run evaluation pipeline
run_evaluation_pipeline()
