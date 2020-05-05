import numpy as np


def cost_(y: np.ndarray, y_hat: np.ndarray):
    if not (y.ndim == 1 and y.size > 0 and y_hat.ndim == 1 and y_hat.size > 0):
        return
    if y.size != y_hat.size:
        return
    y_diff = y_hat - y
    return np.dot(y_diff, y_diff) / (2 * y.size)


if __name__ == '__main__':
    X = np.array([0, 15, -9, 7, 12, 3, -21])
    Y = np.array([2, 14, -13, 5, 12, 4, -19])
    print(cost_(X, Y))