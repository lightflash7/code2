import numpy as np


def gradient_descent(X, Y, theta, alpha, num_iters):
    # num_iters为迭代次数
    m = X.size
    for _ in range(num_iters):
        temp = X@theta-Y
        temp = X.T@temp
        theta = theta - alpha/m*temp
    return theta






