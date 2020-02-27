import numpy as np


def NormalEquations(x, y):
    theta = np.zeros((x.shape[1], 1))
    theta = np.linalg.inv((x.T @ x)) @ x.T @ y
    return theta
