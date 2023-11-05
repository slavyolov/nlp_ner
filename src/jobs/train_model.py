"""
Entry point for the text data processing application
"""
from pyhocon import ConfigFactory
from src.utils.setup_logging import setup_logging
import logging
from transformations.model_training import ModelTraining
import json
from pathlib import Path


logger = logging.getLogger(__name__)


if __name__ == '__main__':
    # Invoke the configuration file :
    config_file = Path(Path(__file__).parents[1], "local_development/conf.json")
    config = ConfigFactory.parse_file(config_file)

    # Setup logger
    setup_logging(config=config)

    # Train model
    input_file = Path(Path(__file__).parents[2], config.tables.intermediate.annotations)
    training_data = json.load(open(input_file, "r"))
    logger.info(f"Number of texts in training data : {len(training_data)}")

    model_cls = ModelTraining(config=config, training_data=training_data)
    model = model_cls.run()

    # Save the  model to directory
    output_dir = str(Path(Path(__file__).parents[2], config.tables.output.model))
    model.to_disk(output_dir)
    logger.info("Saved model to {output_dir}")
    logger.info("Training process completed!")


