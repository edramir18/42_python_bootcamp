from ctypes import Union
import numpy as np


def simple_gradient(x: np.ndarray, y: np.ndarray, theta: np.ndarray):
    if not (x.ndim == 1 and x.size > 0 and y.ndim == 1 and y.size > 0
            and theta.ndim == 1 and theta.size == 2):
        return None
    if x.size != y.size:
        return None
    xp = np.insert(x.reshape(-1,1), 0, values=1, axis=1)
    y_hat = np.dot(xp, theta)
    napla0 = (y_hat - y).sum() / y.size
    napla1 = ((y_hat - y) * x).sum() / y.size
    return np.array([napla0, napla1])


if __name__ == '__main__':
    def test():
        x = np.array(
            [12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733])
        y = np.array(
            [37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554])
        # Example 0:
        theta1 = np.array([2, 0.7])
        arr = simple_gradient(x, y, theta1)
        print(repr(arr))
        # Example 1:
        theta2 = np.array([1, -0.4])
        arr = simple_gradient(x, y, theta2)
        print(repr(arr))

    test()
