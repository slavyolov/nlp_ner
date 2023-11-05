import numpy as np


def write_text_to_file(path, df):
    return df[["texts"]].to_csv(path, header=None, index=None, sep='\n', mode='w')
