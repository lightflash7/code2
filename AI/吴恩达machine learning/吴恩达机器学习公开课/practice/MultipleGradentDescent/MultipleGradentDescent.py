import numpy as np
from GradentDescent import *
from CostFunction import *


def main():
    # ============================数据读取和准备================================
    data = np.loadtxt('ex1data2.txt', delimiter=',', usecols=(0, 1, 2))
    x = data[:, :-1]
    y = data[:, -1]
    y = y.reshape((y.shape[0], 1))
    y = y / 10000  # 单位万元
    i_num = x.shape[0]
    n_num = x.shape[1] + 1  # 补上第一列的个数所以+1

    # ========================设置学习率和迭代次数和初值===========================
    alpha = 0.1
    iterations = 500
    theta = np.zeros((n_num, 1))  # theta成列展开

    # ==============================数据归一化==================================
    x_average = x.mean(axis=0)
    x_average = np.tile(x_average, (i_num, 1))
    x_std = x.std(axis=0)
    x_std = np.tile(x_std, (i_num, 1))
    x = (x - x_average) / x_std
    x = np.c_[np.ones((i_num, 1)), x]  # 最后补上x0那一列（因为第一列标准差为0）

    # ===========================梯度下降算法===================================
    theta = GradentDescent(x, y, theta, alpha, iterations)

    # ================================打印结果===================================
    print(theta)


if __name__ == '__main__':
    main()
