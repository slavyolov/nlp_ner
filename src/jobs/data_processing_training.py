"""
Entry point for the text data processing application
"""
from pyhocon import ConfigFactory
from src.utils.setup_logging import setup_logging
from src.utils.reader import read_csv
from src.utils.writer import write_text_to_file
from transformations.text_processing import ProcessTextData
from pathlib import Path
import logging


logger = logging.getLogger(__name__)


if __name__ == '__main__':
    # Invoke the configuration file :
    config_file = Path(Path(__file__).parents[1], "local_development/conf.json")
    config = ConfigFactory.parse_file(config_file)

    # Setup logger
    setup_logging(config=config)

    # Load input data
    input_df = read_csv(input_path=config.tables.input.urls.path, file_separator=config.tables.input.urls.path)

    # Fetch first N urls
    input_df = input_df[:config.n_urls_for_training]

    # Transform text data
    urls = input_df["urls"].values.tolist()
    text_transformer = ProcessTextData(input_df=input_df)
    texts = text_transformer.run()
    texts = texts[texts["texts"] != 'no_text_returned']

    write_text_to_file(path=Path(Path(__file__).parents[2], config.tables.intermediate.texts),  df=texts)
    texts.to_csv(path_or_buf=Path(Path(__file__).parents[2], 'data/intermediate/texts.csv'), header=None,
                 index=None, sep=',', mode='w')
    logger.info("process completed!")
