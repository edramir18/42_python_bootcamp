import numpy as np
from numpy import ndarray


class ScrapBooker:
    @staticmethod
    def crop(array, dimensions, position=(0, 0)):
        """

        :param ndarray array:
        :param tuple dimensions:
        :param tuple position:
        :return: ndarray
        """
        if dimensions[0] > array.shape[0] or dimensions[1] > array.shape[1]:
            raise ValueError
        if not (0 <= position[0] < array.shape[0]
                and 0 <= position[1] < array.shape[1]):
            raise ValueError
        xbgn = position[0]
        xend = xbgn + dimensions[0]
        ybgn = position[1]
        yend = ybgn + dimensions[1]
        return array[xbgn:xend, ybgn:yend]

    @staticmethod
    def thin(array, n, axis=0):
        if axis == 0:
            return array[::n]
        else:
            return array[:,::n]

    @staticmethod
    def juxtapose(array, n, axis):
        ...

    @staticmethod
    def mosaic(array, dimensions):
        ...