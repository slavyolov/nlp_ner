# Setup logging
import os
import sys
import logging
from pyhocon import ConfigTree
from pathlib import Path
from datetime import datetime


def setup_logging(config: ConfigTree) -> None:
    """

    Args:
        config: ConfigTree
            The configuration tree object containing the project settings

    Returns:

    """
    # one-shot configuration of root logger
    # log basically everything to stdout
    logging.basicConfig(
        level=config.logging.level,
        stream=sys.stdout,
        format="%(asctime)s - %(name)s - [%(levelname)s] - [%(filename)s:%(lineno)d] [%(funcName)s] - %(message)s",
    )

    # configure project logger
    # since it's a child of the root logger, everything that is logged via the project logger is also put to stdout
    project_logger_name = __name__.split(".")[0]  # assuming __name__ is used for module level logger names
    logger = logging.getLogger(project_logger_name)
    logger.setLevel(config.logging.level)
    logger.info("Logging initialized!")
