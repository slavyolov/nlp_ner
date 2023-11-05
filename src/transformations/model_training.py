"""
Model training
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

    def run(self):
        """
        Execute model training

        Returns:

        """
        logger.info(f"Pipeline names : {self.nlp.pipe_names}")

        # Adding labels to the `ner`
        for _, annotations in self.training_data:
            for ent in annotations.get("entities"):
                self.ner.add_label(ent[2])

        # Disable not needed pipeline components
        pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
        unaffected_pipes = [pipe for pipe in self.nlp.pipe_names if pipe not in pipe_exceptions]

        # Train model :
        with self.nlp.disable_pipes(*unaffected_pipes):
            # Training for N number of iterations
            for iteration in range(self.config.model.training.iterations):

                # shuffling examples  before every iteration
                random.shuffle(self.training_data)
                losses = {}

                for text, annotations in self.training_data:
                    # create Example
                    doc = self.nlp.make_doc(text)
                    example = Example.from_dict(doc, annotations)
                    # Update the model
                    self.nlp.update([example], losses=losses, drop=0.3)

                logger.info(f"Losses : {losses}")

        logger.info("Model trained successfully!")

        return self.nlp
