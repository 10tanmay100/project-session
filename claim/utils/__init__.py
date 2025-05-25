import yaml
import os
import pickle
import sys
from claim.exception.exception import InsuranceClaimException
import pandas as pd
from claim.logging.logger import logging
def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns its contents as a Python dictionary.

    Args:
        file_path (str): The path to the YAML file.

    Returns:
        dict: Parsed contents of the YAML file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        yaml.YAMLError: If there's an error parsing the YAML file.
        Exception: For any other exceptions that may occur.
    """
    try:
        logging.info("Entered the read_yaml_file method of MainUtils class")
        # Open and read the YAML file
        with open(file_path, 'r') as file:
            logging.info(f"Reading YAML file from {file_path}")
            data = yaml.safe_load(file)
            return data

    except Exception as e:
        # Handle other exceptions and provide traceback
        logging.error(f"Error reading YAML file: {e}")
        raise InsuranceClaimException(e, sys)