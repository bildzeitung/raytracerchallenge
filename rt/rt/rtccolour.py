"""
    Colour representation
"""

from . import Tuple


class Colour(Tuple):
    def __init__(self, r: float, g: float, b: float):
        super().__init__(r, g, b, 0)

    @property
    def red(self):
        return self._t[0]

    @property
    def green(self):
        return self._t[1]

    @property
    def blue(self):
        return self._t[2]
