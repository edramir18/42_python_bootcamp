import numpy as np


def predict_(x: np.ndarray, theta: np.ndarray):
    if not (isinstance(x, np.ndarray) and isinstance(theta, np.ndarray)):
        return None
    if not(x.ndim == 1 and x.size > 0 and theta.ndim == 1 and theta.size == 2):
        return None
    x = np.insert(x.reshape(-1, 1), 0, values=1, axis=1)
    return np.dot(x, theta).astype(float)


if __name__ == '__main__':
    x0 = np.arange(1, 6)
    theta1 = np.array([5, 0])
    print(predict_(x0, theta1))
    theta2 = np.array([0, 1])
    print(predict_(x0, theta2))
    theta3 = np.array([5, 4])
    print(predict_(x0, theta3))
    theta4 = np.array([-3, 1])
    print(predict_(x0, theta4))
