"""
Common utility functions used across the package
"""
import numpy as np
from typing import List


def _getVertGauss(width: int, height: int, offset: int, sigma: float) -> List[float]:
    linspace = np.linspace(0, width, width)
    gauss_mean = width // 2 + offset
    gauss_sd = sigma

    gauss_1d = np.exp(-np.square(linspace - gauss_mean) / (2 * np.square(gauss_sd)))
    gauss_vertline = np.atleast_2d(gauss_1d).T
    gauss_vertline = np.tile(gauss_vertline, height).T

    return gauss_vertline


def _getHorzGauss(width: int, height: int, offset: int, sigma: float) -> List[float]:
    linspace = np.linspace(0, height, height)
    gauss_mean = height // 2 + offset
    gauss_sd = sigma

    gauss_1d = np.exp(-np.square(linspace - gauss_mean) / (2 * np.square(gauss_sd)))
    gauss_horzline = np.atleast_2d(gauss_1d).T
    gauss_horzline = np.tile(gauss_horzline, width)

    return gauss_horzline


def _getSmoothCircle(width: int, height: int, sigma: float, offsetH: int = 0, offsetW: int = 0) -> List[float]:
    # Heights (hs) and Widths (ws)
    # Avoid using x and y
    hs, ws = np.mgrid[0:height, 0:width]

    circle = np.exp(
        -(
            np.square(hs - (height // 2 + offsetH)) / (2 * np.square(sigma))
            + np.square(ws - (width // 2 + offsetW)) / (2 * np.square(sigma))
        )
    )

    return circle
