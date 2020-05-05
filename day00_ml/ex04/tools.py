import numpy as np


def add_intercept(x: np.ndarray):
    if not isinstance(x, np.ndarray):
        return None
    return np.insert(x.reshape(-1, 1), 0, values=1, axis=1).astype(float)


if __name__ == '__main__':
    y = np.arange(1,10).reshape(3,3)
    print(add_intercept(y))
    y = np.array(range(10))
    print(add_intercept(y))
