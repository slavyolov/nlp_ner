# Setup logging
import sys
import logging
from pyhocon import ConfigTree


def setup_logging(config: ConfigTree) -> None:
    """

    Args:
        config: ConfigTree
            The configuration tree object containing the project settings

    Returns:

    """
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        format="%(asctime)s - %(name)s - [%(levelname)s] - [%(filename)s:%(lineno)d] [%(funcName)s] - %(message)s",
    )

    # configure project logger
    # since it's a child of the root logger, everything that is logged via the project logger is also put to stdout
    project_logger_name = __name__.split(".")[0]  # assuming __name__ is used for module level logger names
    logger = logging.getLogger(project_logger_name)
    logger.setLevel(config.logging["level"])
    logger.info("Logging initialized!")
