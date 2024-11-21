from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_data_path: Path
    status_file_path: Path
    all_schema: dict

@dataclass
class PreprocessingConfig:
    root_dir: Path
    raw_data_path: Path
    train_data_path: Path
    test_data_path: Path
    status_file_path: Path

@dataclass
class TrainingConfig:
    root_dir: Path
    train_data_path: Path
    model_path: Path