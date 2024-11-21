import os
from FakeNewsDetection import logger
import pandas as pd
from FakeNewsDetection.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
    def validate_data_columns(self) ->bool:
        try:
            val_status = None
            data = pd.read_csv(self.config.unzip_data_path, nrows=5)
            all_cols = list(data.columns)

            all_schema_cols = list(self.config.all_schema.keys())

            for col in all_cols:
                if col not in all_schema_cols:
                    logger.error(f"Column {col} is not in schema")
                    val_status=False
                    break
            else:
                val_status = True
            

            with open(self.config.status_file_path, "w") as f:
                f.write(f"Validation Status: {val_status}")
                if val_status:
                    logger.info("Data Validation Passed")

            return val_status
        except Exception as e:
            logger.error(f"Error in data validation: {str(e)}")
            raise Exception()


