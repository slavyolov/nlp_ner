"""
Model predictions
"""
import spacy
from transformations.abstract_transformer import AbstractTransformer
import logging
import random
from spacy.training.example import Example
from pyhocon import ConfigTree


logger = logging.getLogger(__name__)


class ModelTraining(AbstractTransformer):
    def __init__(self, config: ConfigTree, training_data: list):
        self.config = config
        self.nlp = spacy.load('en_core_web_sm')  # load pre-existing spacy model
        self.training_data = training_data
        self.ner = self.nlp.get_pipe("ner")

    def predict(self):
        """
        Predictions using already trained model

        Returns:

        """
        doc = self.nlp("I was driving a Alto")
        print("Entities", [(ent.text, ent.label_) for ent in doc.ents])