import numpy as np


def CostFunction(x, y, theta):
    m = x.size
    x = x.reshape((m, 1))  # 一维变成二维才能hstake拼接(另一种方法是用np.c_())
    y = y.reshape((m, 1))
    X = np.hstack((np.ones((m, 1)), x))
    # cost = ((X @ theta.T - y) ** 2) / 2 / m
    cost = X @ theta - y
    cost = cost ** 2
    cost = cost / 2 / m
    cost = cost.sum()
    return cost