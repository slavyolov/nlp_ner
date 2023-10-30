import pandas as pd
from pathlib import Path
from typing import Union
import logging


logger = logging.getLogger(__name__)


def read_csv(input_path: Union[Path, str], file_separator: str, check_data: bool = True):
    file_path = Path(Path(__file__).parents[2], input_path)
    df = pd.read_csv(filepath_or_buffer=file_path, sep=file_separator, header=0, on_bad_lines='skip')

    # check data loss due to bad lines
    if check_data:
        lines_at_start = count_lines_enumerate(file_path)
        lines_at_end = len(df)
        pct_missing = 1 - (lines_at_end/lines_at_start)
        logger.info(
            f"{pct_missing * 100:.2f}% of the input data is lost due to bad lines"
        )

    return df


def count_lines_enumerate(file_name):
    """
    Count the number of lines in a file

    Args:
        file_name:

    Returns:

    """
    line_count = 0

    # Read the input file and return the line count
    fp = open(file_name, 'r')
    for line_count, line in enumerate(fp):
        pass
    return line_count
