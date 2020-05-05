import numpy as np
import matplotlib.pyplot as plt


def plot_with_cost(x: np.ndarray, y: np.ndarray, theta: np.ndarray):
    if not (x.ndim == 1 and x.size > 0 and y.ndim == 1 and y.size > 0
            and theta.ndim == 1 and theta.size == 2):
        return
    y_hat = np.dot(np.insert(x.reshape((-1,1)), 0, values=1, axis=1), theta)
    plt.plot(x, y, 'o', x, y_hat, 'k')
    for k, v in enumerate(x):
        x_p = np.empty(2)
        x_p.fill(v)
        y_p = np.array([y[k], y_hat[k]])
        plt.plot(x_p, y_p, '--k')
    plt.show()


if __name__ == '__main__':
    X = np.arange(1, 6)
    Y = np.array(
        [11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568])
    # Example 1:
    theta1 = np.array([18, -1])
    plot_with_cost(X, Y, theta1)

    theta2 = np.array([14, 0])
    plot_with_cost(X, Y, theta2)
    theta3 = np.array([12, 0.8])
    plot_with_cost(X, Y, theta3)