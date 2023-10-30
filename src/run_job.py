"""
Entry point for the application
"""
from utils.data_profiling import data_profiling
from pyhocon import ConfigFactory
import pandas as pd
from src.utils.setup_logging import setup_logging
from src.utils.reader import read_csv



if __name__ == '__main__':
    # Invoke the configuration file :
    config_file = "./local_development/conf.json"
    config = ConfigFactory.parse_file(config_file)

    # Setup logger
    setup_logging(config=config)

    if config.run_profiling:
        # Run data profiling
        for table_key, table_details in config.tables.input.items():
            data_profiling(input_path=table_details.path, file_separator=table_details.sep,
                           output_path=config.tables.intermediate.base_path)

    # Load input data
    facebook_df = read_csv(input_path=config.tables.input.facebook.path,
                           file_separator=config.tables.input.facebook.sep)
    google_df = read_csv(input_path=config.tables.input.google.path,
                         file_separator=config.tables.input.google.sep)
    website_df = read_csv(input_path=config.tables.input.website.path,
                           file_separator=config.tables.input.website.sep)
    print("done")