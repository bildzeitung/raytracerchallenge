""" Tuple representation class
"""
import numpy as np


class Tuple:
    """ (x, y, z, w)

        for w == 0, it's a vector
        for w == 1, it's a point
    """

    def __init__(self, x: float, y: float, z: float, w: float, narray=None):
        if narray is not None:
            self._t = narray
        else:
            self._t = np.array((x, y, z, w))

    @property
    def x(self):
        return self._t[0]

    @property
    def y(self):
        return self._t[1]

    @property
    def z(self):
        return self._t[2]

    @property
    def w(self):
        return self._t[3]

    def __eq__(self, other):
        return (self._t == other._t).all()

    def __add__(self, other):
        return Tuple(0, 0, 0, 0, self._t + other._t)

    def __neg__(self):
        return Tuple(0, 0, 0, 0, -self._t)

    def __mul__(self, other):
        return Tuple(0, 0, 0, 0, self._t * other)

    def __truediv__(self, other):
        return Tuple(0, 0, 0, 0, self._t / other)


class Point(Tuple):
    """ a point is a tuple with w == 1
    """

    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, 1)

    def __sub__(self, other):
        """ Returns a Vector
        """
        return Tuple(0, 0, 0, 0, self._t - other._t)


class Vector(Tuple):
    """ a vector is a tuple with w == 0
    """

    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, 0)
        self._magnitude = None
        self._norm = None

    @property
    def magnitude(self):
        if not self._magnitude:
            self._magnitude = np.linalg.norm(self._t)
        return self._magnitude

    @property
    def norm(self):
        if not self._norm:
            result = self._t / self.magnitude
            self._norm = Vector(result[0], result[1], result[2])
        return self._norm

    def __sub__(self, other):
        return Tuple(0, 0, 0, 0, self._t - other._t)


def make_tuple(x: float, y: float, z: float, w: float) -> Tuple:
    if w == 0:
        return Vector(x, y, z)
    elif w == 1:
        return Point(x, y, z)

    return Tuple(x, y, z, w)


def dot(a: Tuple, b: Tuple) -> float:
    return np.dot(a._t, b._t)


def cross(a: Vector, b: Vector) -> Vector:
    v = np.cross(a._t[0:3], b._t[0:3])
    print(v[0], v[1], v[2])
    return Vector(v[0], v[1], v[2])
