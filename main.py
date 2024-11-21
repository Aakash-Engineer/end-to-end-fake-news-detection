from FakeNewsDetection.pipeline.step_1_data_ingestion import run_data_ingestion_pipeline
from FakeNewsDetection.pipeline.step_2_data_validation import run_data_validation_pipeline
from FakeNewsDetection.pipeline.step_3_data_preprocessing import run_data_preprocessing_pipeline


# run data ingestion pipeline
run_data_ingestion_pipeline()

# run data validation pipeline
run_data_validation_pipeline()

# run data preprocessing pipeline
run_data_preprocessing_pipeline()
