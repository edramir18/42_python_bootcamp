import numpy as np


def simple_predict(x: np.ndarray, theta: np.ndarray):
    if not (isinstance(x, np.ndarray) and isinstance(theta, np.ndarray)):
        return None
    if x.ndim > 1 or not (theta.ndim == 1 and theta.size == 2):
        return None
    if x.size == 0 or theta.size == 0:
        return None
    c = [x0 * theta[1] + theta[0] for x0 in x]
    return np.array(c, dtype=float)


if __name__ == '__main__':
    x = np.arange(1, 6)
    theta1 = np.array([5, 0])
    print(simple_predict(x, theta1))

    theta2 = np.array([0, 1])
    print(simple_predict(x, theta2))

    theta3 = np.array([5, 3])
    print(simple_predict(x, theta3))

    theta4 = np.array([-3, 1])
    print(simple_predict(x, theta4))

