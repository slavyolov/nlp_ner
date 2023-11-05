"""
Process text data for model training or predictions
"""
import bs4
import pandas as pd
from transformations.abstract_transformer import AbstractTransformer
import logging
from urlextract import URLExtract
import nltk
import re
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request


nltk.download('punkt')
logger = logging.getLogger(__name__)


class ProcessTextData(AbstractTransformer):
    def __init__(self, input_df: pd.DataFrame):
        self.input_df = input_df

    def run(self):
        self.input_df["texts"] = self.input_df["urls"].apply(lambda x: self._extract_only_visible_content(x))
        self.input_df["texts"] = self.input_df["texts"].apply(lambda x: self._remove_html_tags(x))
        self.input_df["texts"] = self.input_df["texts"].apply(lambda x: self._remove_intervals(x))
        self.input_df["texts"] = self.input_df["texts"].apply(lambda x: self._remove_urls(x))
        self.input_df["texts"] = self.input_df["texts"].apply(lambda x: self._remove_characters(x))
        self.input_df["texts"] = self.input_df["texts"].apply(lambda x:
                                                              self.replace_multiple_intervals_with_single_interval(x))

        return self.input_df

    @staticmethod
    def _tag_visible(element):
        """
        Tag visible elements

        Args:
            element:

        Returns:

        """
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True

    def _extract_only_visible_content(self, url: str) -> str:
        """
        Select only the visible elements from the url

        Args:
            url:

        Returns:

        """
        try:
            response = urllib.request.urlopen(url).read()
            soup = BeautifulSoup(response, 'html.parser')
            texts = soup.findAll(text=True)
            visible_texts = filter(self._tag_visible, texts)
            return u" ".join(t.strip() for t in visible_texts)
        except Exception as e:
            logger.warning(f"Page content from url {url} was not obtained - reason {e}")
            return "no_text_returned"

    @staticmethod
    def _remove_html_tags(text) -> str:
        """
        Remove html tags

        Args:
            text: input text to clear

        Returns:

        """
        soup = bs4.BeautifulSoup(text, 'html.parser')
        return soup.get_text()

    @staticmethod
    def _remove_intervals(text: str) -> str:
        """
        Remove intervals at the begin and end of a string

        Args:
            text: input text to clear

        Returns:

        """
        return text.strip()

    @staticmethod
    def _remove_urls(text: str) -> str:
        """
        Replace the URLS from text with space/interval

        Args:
            text:

        Returns:

        """
        extractor = URLExtract()  # create an URLExtract object which will be used to extract URLs from the text
        urls = extractor.find_urls(text)

        for url in urls:
            text = text.replace(url, " ")

        return text

    @staticmethod
    def _remove_characters(text: str) -> str:
        """
        Remove special characters and symbols

        Args:
            text:

        Returns:

        """
        text = text.replace('\n', ' ')
        text = text.replace('\n\n', ' ')
        text = text.replace('\n\n\n', ' ')
        text = text.replace('&', ' ')
        text = text.replace('#', '')
        text = text.replace('x200B', ' ')
        text = text.replace('[', ' ')
        text = text.replace(']', ' ')
        text = text.replace('(', ' ')
        text = text.replace(')', ' ')
        text = text.replace('|', ' ')
        text = text.replace(':-', '')
        text = text.replace('~', '')
        text = text.replace('~~', '')
        text = text.replace('-', ' ')
        text = text.replace('\\', '')
        text = text.replace('*', '')
        text = text.replace('!', '')
        text = text.replace('?', '')
        return text

    @staticmethod
    def replace_multiple_intervals_with_single_interval(text: str):
        return re.sub(' +', ' ', text)
