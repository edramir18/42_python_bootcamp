from typing import Union, Optional

import numpy as np


def cost_elem_(y: np.ndarray, y_hat: np.ndarray) -> Union[np.ndarray, None]:
    if not (y.ndim == 2 and y.shape[1] == 1
            and y_hat.ndim == 2 and y_hat.shape[1] == 1):
        return
    if y.size != y_hat.size:
        return
    d2 = (y_hat - y) ** 2
    return d2 / (2 * y.size)


def cost_(y: np.ndarray, y_hat: np.ndarray):
    if not (y.ndim == 2 and y.shape[1] == 1
            and y_hat.ndim == 2 and y_hat.shape[1] == 1):
        return None
    cost = cost_elem_(y, y_hat)
    return cost.sum()


if __name__ == '__main__':
    def test():
        x1 = np.array(range(0,5)).reshape((-1,1)).astype(float)
        theta1 = np.array([2, 4]).reshape((-1, 1)).astype(float)
        y_hat1 = np.dot(np.insert(x1, 0, values=1, axis=1), theta1)
        y1 = np.array([2, 7, 12, 17, 22]).reshape(-1, 1).astype(float)
        print(cost_elem_(y1, y_hat1))
        print(cost_(y1, y_hat1))
        x2 = np.array(
            [[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
        theta2 = np.array([[0.05], [1.], [1.], [1.]])
        y_hat2 = np.dot(np.insert(x2, 0, values=1, axis=1), theta2)
        y2 = np.array([[19.], [42.], [67.], [93.]])
        print(cost_elem_(y2, y_hat2))
        print(cost_(y2, y_hat2))


    test()
