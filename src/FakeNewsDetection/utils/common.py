import yaml
from box import ConfigBox
import os
from pathlib import Path
from FakeNewsDetection import logger
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from typing import Any
import json


@ensure_annotations
def read_yaml(file_path: Path) -> ConfigBox:
    """Read Yaml file
    Args:   
        file_path: Path to the yaml file
    Raises:
        BoxError: If the file is not found
    Returns:
        ConfigBox object
    """

    try:
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
            logger.info(f'Loaded yaml file from {file_path}')
            return ConfigBox(config)
        
    except BoxValueError:
        raise ValueError(f'Error reading yaml file from {file_path}')
    except Exception as e:
        logger.error(f'Error reading yaml file from {file_path}')
        raise e
        


@ensure_annotations
def create_directory(paths: list, verbose=True):
    """Create directory
    Args:   
        paths: List of paths to be created
        verbose: Print the path created
    Raises:
        None
    Returns:
        None
    """
    for path in paths:
        Path(path).mkdir(parents=True, exist_ok=True)
        if verbose:
            logger.info(f'Created directory {path}')


@ensure_annotations
def save_json(path: Path, data: dict):
    """Save json file
    Args:
        path: Path to save the json file
        data: Data to be saved
    Raises:
        None
    Returns:    
        None
    """
    try:
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
            logger.info(f'Saved json file to {path}')
    except Exception as e:
        logger.error(f'Error saving json file to {path}')
        raise e