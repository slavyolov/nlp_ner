"""
Entry point for the application
"""
from pyhocon import ConfigFactory
from src.utils.setup_logging import setup_logging
from src.utils.reader import read_csv
from transformations.web_crawling import ProcessTextData
import csv
from pathlib import Path


if __name__ == '__main__':
    # Invoke the configuration file :
    config_file = "./local_development/conf.json"
    config = ConfigFactory.parse_file(config_file)

    # Setup logger
    setup_logging(config=config)

    # Load input data
    input_df = read_csv(input_path=config.tables.input.urls.path, file_separator=config.tables.input.urls.path)

    # # get rid of the header
    # urls = urls[1:]
    #
    # Fetch first N urls
    input_df = input_df[:config.n_urls_for_training]
    #
    # Transform text data
    urls = input_df["urls"].values.tolist()
    text_transformer = ProcessTextData(input_df=input_df)
    texts = text_transformer.run()

    print("done")


import bs4
import requests
from transformations.abstract_ransformer import AbstractTransformer


def extract_from_text(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    return [soup.body.get_text(' ', strip=True)]

import time
start_time = time.time()
input_df["texts"] = input_df["urls"].apply(lambda x: extract_from_text(x))
print("--- %s seconds ---" % (time.time() - start_time))

# definition of product (Google): an article or substance that is manufactured or refined for sale.
