"""
Implements abstract class Mask

Building methods for basic shapes such as line and circle
"""
import numpy as np
from src import utils as srcutils
from typing import List
from src import classes


class ShapeMask(classes.Mask):
    def __init__(self, shape: tuple) -> None:
        super(ShapeMask, self).__init__(shape)

    def verticalLine(
        self,
        radius: int = 0,
        sigma: float = 0.0,
        offset: int = 0,
        topcut: int = 0,
        bottomcut: int = 0,
    ):
        # Perhaps in the future, position should be added and used instead of offset
        try:
            if radius < 0 or radius >= self.width // 2:
                raise ValueError("'width' argument must be a positive integer")
            if sigma < 0.0:
                raise ValueError("'sigma' must be positive")
            if abs(offset) > self.width // 2:
                raise ValueError("'offset' must be within image's shape")
            if topcut < 0 or topcut >= self.height // 2:
                raise ValueError("'topcut' cuts too much")
            if bottomcut < 0 or bottomcut >= self.height // 2:
                raise ValueError("'bottomcut' cuts too much")
        except ValueError as err:
            print("\n{}: {}".format(type(err).__name__, err))

        if np.isclose(sigma, 0):
            if bottomcut == 0:
                self._array[
                    topcut:,
                    (self.width // 2 + offset)
                    - radius : (self.width // 2 + offset)
                    + radius,
                ] = 1
            else:
                self._array[
                    topcut:-bottomcut,
                    (self.width // 2 + offset)
                    - radius : (self.width // 2 + offset)
                    + radius,
                ] = 1
        else:
            vertgauss = srcutils._getVertGauss(self.width, self.height, offset, sigma)

            self._array = np.fmax(self._array, vertgauss)

        return self

    def horizontalLine(
        self,
        radius: int = 0,
        sigma: float = 0.0,
        offset: int = 0,
        leftcut: int = 0,
        rightcut: int = 0,
    ):
        # Repetitive code?
        try:
            if radius < 0 or radius >= self.width // 2:
                raise ValueError("'width' argument must be a positive integer")
            if sigma < 0.0:
                raise ValueError("'sigma' must be positive")
            if abs(offset) > self.width // 2:
                raise ValueError("'offset' must be within image's shape")
            if leftcut < 0 or leftcut >= self.height // 2:
                raise ValueError("'leftcut' cuts too much")
            if rightcut < 0 or rightcut >= self.height // 2:
                raise ValueError("'rightcut' cuts too much")
        except ValueError as err:
            print("\n{}: {}".format(type(err).__name__, err))

        if np.isclose(sigma, 0):
            if rightcut == 0:
                self._array[
                    (self.height // 2 + offset)
                    - radius : (self.height // 2 + offset)
                    + radius,
                    leftcut:,
                ] = 1
            else:
                self._array[
                    (self.height // 2 + offset)
                    - radius : (self.height // 2 + offset)
                    + radius,
                    leftcut:-rightcut,
                ] = 1
        else:
            horzgauss = srcutils._getHorzGauss(self.width, self.height, offset, sigma)

            self._array = np.fmax(self._array, horzgauss)

        return self

    def circle(
        self, radius: int = 0, sigma: float = 0.0, offsetH: int = 0, offsetW: int = 0
    ):
        # Repetitive code?
        try:
            if radius < 0 or radius >= self.width // 2:
                raise ValueError("'width' argument must be a positive integer")
            if sigma < 0.0:
                raise ValueError("'sigma' must be positive")
            for offset in [offsetH, offsetW]:
                if abs(offset) > self.width // 2:
                    raise ValueError("'offset' must be within image's shape")
        except ValueError as err:
            print("\n{}: {}".format(type(err).__name__, err))

        if np.isclose(sigma, 0):
            # Heights (hs) and widths (ws)
            # Avoid using xs and ys (x & y is not universally consistent among other libraries such as OpenCV)
            hs, ws = np.mgrid[0 : self.height, 0 : self.width]

            self._array[
                (hs - (self.height // 2 + offset)) ** 2
                + (ws - (self.width // 2 + offset)) ** 2
                < radius**2
            ] = 1
        else:
            smoothCircle = srcutils._getSmoothCircle(
                self.width, self.height, sigma, offsetH, offsetW
            )

            self._array = np.fmax(self._array, smoothCircle)

        return self
