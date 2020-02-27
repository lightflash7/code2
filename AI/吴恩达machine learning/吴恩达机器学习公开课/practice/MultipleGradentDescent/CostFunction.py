import numpy as np


# 计算代价
def CostFunction(x, y, theta):
    cost = np.sum(((x @ theta - y) ** 2) / 2 / x.shape[0])
    return cost
