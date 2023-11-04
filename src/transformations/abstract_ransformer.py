"""
Blueprint for data transformations
"""
from abc import abstractmethod


class AbstractTransformer:
    """Abstract Transformer Class"""
    @abstractmethod
    def run(self, *args, **kwargs):
        """Abstract transform method"""
        raise NotImplementedError
