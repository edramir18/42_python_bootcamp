import matplotlib.pyplot as plt
import numpy as np


def plot(x: np.ndarray, y: np.ndarray, theta:np.ndarray):
    if not(isinstance(x, np.ndarray) and isinstance(y, np.ndarray)
           and isinstance(theta, np.ndarray)):
        return
    if not(x.ndim == 1 and x.size > 0 and y.ndim == 1 and y.size > 0
           and theta.size == 2 and theta.ndim == 1):
        return
    xl = np.dot(np.insert(x.reshape(-1, 1), 0, values=1, axis=1), theta)
    poly1d_fn = np.poly1d(theta)
    plt.plot(x, y, 'o', x, xl, 'k')
    plt.show()


if __name__ == '__main__':
    x = np.arange(1, 6)
    y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])
    theta1 = np.array([4.5, -0.2])
    plot(x, y, theta1)
    theta2 = np.array([-1.5, 2])
    plot(x, y, theta2)
    theta3 = np.array([3, 0.3])
    plot(x, y, theta3)
