import numpy as np
from CostFunction import *


# 梯度下降算法
def GradentDescent(x, y, theta, alpha, iterations):
    for _ in range(iterations):
        temp = x.dot(theta) - y
        temp = temp.T.dot(x)
        temp = temp.reshape((temp.size, 1))
        theta = theta - temp * alpha / x.shape[0]
        print('J=', CostFunction(x, y, theta))
    return theta
