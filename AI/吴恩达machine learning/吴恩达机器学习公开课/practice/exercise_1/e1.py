import matplotlib.pyplot as plt
import GradientDescent as gd
from CostFunction import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def main():
    # ===============================导入数据===================================
    data = np.loadtxt('ex1data1.txt', delimiter=',', usecols=(0, 1))
    x = data[:, 0]
    y = data[:, 1]

    # ===============================数据准备===================================
    m = x.size
    theta = np.zeros((2, 1))
    interations = 3000
    alpha = 0.01
    X = np.c_[np.ones((m, 1)), x]
    Y = y[:, np.newaxis]

    # ===============================梯度下降算法 ===============================
    theta = gd.gradient_descent(X, Y, theta, alpha, interations)
    print('theta0的结果是', theta[0], '，', 'theta1的结果是', theta[1])

    # ===============================画图示意====================================
    plt.figure(0)
    plt.xlabel('Population of City in 10,000s')
    plt.ylabel('Profit in $10,000s')
    plt.scatter(x, y)
    t = np.arange(0, 23, 0.01)
    z = theta[0] + theta[1] * t
    plt.plot(t, z, 'r')
    # plt.show()
    # plt.pause(1)
    # plt.close()
    # t=np.arange()

    # ================================计算代价====================================
    # theta = np.array((0, 0))
    cost = CostFunction(x, y, theta)
    print('最小代价是', cost)

    # =============================将代价函数可视化================================
    theta_0 = np.linspace(-10, 10, 100)
    theta_1 = np.linspace(-1, 4, 100)
    m1 = theta_0.size
    m2 = theta_1.size
    cost = np.zeros((m1, m2))
    theta_0, theta_1 = np.meshgrid(theta_0, theta_1)
    for i in range(m1):
        for j in range(m2):
            theta2 = np.array([[theta_0[i, j]], [theta_1[i, j]]])
            cost[i, j] = CostFunction(x, y, theta2)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(theta_0, theta_1, cost)
    plt.figure()
    plt.contour(theta_0, theta_1, cost, levels=20)
    plt.scatter(theta[0], theta[1], c='r', marker='x')
    # plt.show()
    plt.pause(10)
    plt.close()


if __name__ == '__main__':
    main()
