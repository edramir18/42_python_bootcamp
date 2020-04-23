import numpy as np
from numpy.random import default_rng


class NumPyCreator:
    def __init__(self):
        self.rng = default_rng()

    def from_list(self, lst, dtype=None):
        if not isinstance(lst, list):
            raise TypeError
        return np.array(lst, dtype=dtype)

    def from_tuple(self, tpl, dtype=None):
        if not isinstance(tpl, tuple):
            raise TypeError
        return np.array(tpl, dtype=dtype)

    def from_random(self, shape, dtype=None):
        if not isinstance(shape, tuple):
            raise TypeError
        return self.rng.standard_normal(shape, dtype)

    def from_iterable(self, itr, dtype=None):
        try:
            iter(itr)
            return np.array(itr, dtype=dtype)
        except TypeError:
            raise TypeError

    def from_shape(self, shape, value=0, dtype=None):
        if not isinstance(shape, tuple):
            raise TypeError
        return np.full(shape, value, dtype=dtype)

    @staticmethod
    def identity(n, dtype=None):
        return np.identity(n, dtype=dtype)
