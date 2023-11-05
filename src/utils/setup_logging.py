# Setup logging
import os
import sys
import logging
from pyhocon import ConfigTree
from pathlib import Path
from datetime import datetime


def setup_logging(config: ConfigTree, to_console: bool = True) -> None:
    """

    Args:
        config: ConfigTree
            The configuration tree object containing the project settings
        to_console : boolean that determines if log messages are written to stdout or to a log file

    Returns:

    """
    # configure project logger
    # since it's a child of the root logger, everything that is logged via the project logger is also put to stdout
    project_logger_name = __name__.split(".")[0]  # assuming __name__ is used for module level logger names
    logger = logging.getLogger(project_logger_name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - [%(levelname)s] - [%(filename)s:%(lineno)d] [%(funcName)s] - %(message)s")

    if to_console:
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(config.logging["level"])
        stdout_handler.setFormatter(formatter)
        logger.addHandler(stdout_handler)
    else:
        run = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_path = Path(Path(__file__).parents[2], ".project_log_files", run)
        os.makedirs(log_path, exist_ok=True)
        log_file = Path(log_path, "app.log")

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(config.logging["level"])
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    logger.info("Logging initialized!")
