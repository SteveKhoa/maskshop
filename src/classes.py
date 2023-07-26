"""
Common classes used across the package
"""
import numpy as np
from typing import List


class Mask:
    """
    Base class for Mask data structure classes
    """

    def __init__(self, shape: tuple = (0, 0)) -> None:
        self._array = np.zeros(shape, np.float32)
        self.shape = shape

        self.height = self.shape[0]
        self.width = self.shape[1]

    def make(self, makeInt: bool = False) -> List[float]:
        if makeInt:
            return np.round(self._array*255).astype(np.uint8)
        else:
            return self._array