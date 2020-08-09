import numpy as np
import os
import argparse
import matplotlib.pyplot as plt
from get_values import get_values_n1, get_values_n2, get_values_n3, get_values_n4, get_values_n6


def get_argument():
    parser = argparse.ArgumentParser(description="Solve equation system using Newton-Raphson")
    parser.add_argument("-T2", help="Nhiệu độ vừng khử", type=int, default=750.0)   # 750, 800, 850, 900
    return parser.parse_args()


def plot_graphs(path: str, T2: float):
    (n1_percents, n1_values) = get_values_n1(path, T2)
    print("% C:   {}".format(n1_percents))

    (n2_percents, n2_values) = get_values_n2(path, T2)
    print("% H2:  {}".format(n2_percents))

    (n3_percents, n3_values) = get_values_n3(path, T2)
    print("% CO:  {}".format(n3_percents))

    (n4_percents, n4_values) = get_values_n4(path, T2)
    print("% CO2: {}".format(n4_percents))

    (n6_percents, n6_values) = get_values_n6(path, T2)
    print("% CH4: {}".format(n6_percents))

    ER = np.array([0.2, 0.25, 0.3, 0.35, 0.4])
    fig, axes = plt.subplots(figsize=(7, 5))
    # print(matrix[:, 0])
    # expected_1 = getExpectation(solution=matrix[:, 0])
    axes.plot(ER, n1_percents, 'c', label='C', linewidth=1)
    axes.plot(ER, n2_percents, 'g--', label=r'$H_2$', linewidth=1)
    axes.plot(ER, n3_percents, 'r', label='CO', linewidth=1)
    axes.plot(ER, n4_percents, 'b--', label='$CO_2$', linewidth=1)
    axes.plot(ER, n6_percents, 'y', label='$CH_4$', linewidth=1)

    axes.scatter(ER, n1_percents, marker='s', color='r')
    axes.text(ER[0], n1_percents[0], r'${}$'.format(round(n1_percents[0],2 )), fontsize=8)
    axes.text(ER[1], n1_percents[1], r'${}$'.format(round(n1_percents[1],2 )), fontsize=8)
    axes.text(ER[2], n1_percents[2], r'${}$'.format(round(n1_percents[2],2 )), fontsize=8)
    axes.text(ER[3], n1_percents[3], r'${}$'.format(round(n1_percents[3],2 )), fontsize=8)
    axes.text(ER[4], n1_percents[4], r'${}$'.format(round(n1_percents[4],2 )), fontsize=8)

    axes.scatter(ER, n2_percents, marker='D', color='g')
    axes.text(ER[0], n2_percents[0], r'${}$'.format(round(n2_percents[0],2 )), fontsize=8)
    axes.text(ER[1], n2_percents[1], r'${}$'.format(round(n2_percents[1],2 )), fontsize=8)
    axes.text(ER[2], n2_percents[2], r'${}$'.format(round(n2_percents[2],2 )), fontsize=8)
    axes.text(ER[3], n2_percents[3], r'${}$'.format(round(n2_percents[3],2 )), fontsize=8)
    axes.text(ER[4], n2_percents[4], r'${}$'.format(round(n2_percents[4],2 )), fontsize=8)

    axes.scatter(ER, n3_percents, marker='X', color='c')
    axes.text(ER[0], n3_percents[0], r'${}$'.format(round(n3_percents[0],2 )), fontsize=8)
    axes.text(ER[1], n3_percents[1], r'${}$'.format(round(n3_percents[1],2 )), fontsize=8)
    axes.text(ER[2], n3_percents[2], r'${}$'.format(round(n3_percents[2],2 )), fontsize=8)
    axes.text(ER[3], n3_percents[3], r'${}$'.format(round(n3_percents[3],2 )), fontsize=8)
    axes.text(ER[4], n3_percents[4], r'${}$'.format(round(n3_percents[4],2 )), fontsize=8)

    axes.scatter(ER, n4_percents, marker='d', color='b')
    axes.text(ER[0], n4_percents[0], r'${}$'.format(round(n4_percents[0],2 )), fontsize=8)
    axes.text(ER[1], n4_percents[1], r'${}$'.format(round(n4_percents[1],2 )), fontsize=8)
    axes.text(ER[2], n4_percents[2], r'${}$'.format(round(n4_percents[2],2 )), fontsize=8)
    axes.text(ER[3], n4_percents[3], r'${}$'.format(round(n4_percents[3],2 )), fontsize=8)
    axes.text(ER[4], n4_percents[4], r'${}$'.format(round(n4_percents[4],2 )), fontsize=8)

    axes.scatter(ER, n6_percents, marker='*', color='y')
    axes.text(ER[0], n6_percents[0], r'${}$'.format(round(n6_percents[0],2 )), fontsize=8)
    axes.text(ER[1], n6_percents[1], r'${}$'.format(round(n6_percents[1],2 )), fontsize=8)
    axes.text(ER[2], n6_percents[2], r'${}$'.format(round(n6_percents[2],2 )), fontsize=8)
    axes.text(ER[3], n6_percents[3], r'${}$'.format(round(n6_percents[3],2 )), fontsize=8)
    axes.text(ER[4], n6_percents[4], r'${}$'.format(round(n6_percents[4],2 )), fontsize=8)


    axes.set_xlabel("ER", fontsize=10)
    axes.set_ylabel("Syngas Compositions (%)", fontsize=10)
    axes.set_xticks(ER)
    axes.set_title(str(int(T2)) + r"$^{o} C$", fontsize=12)
    plt.grid(True, linestyle =':')
    plt.legend(loc='best')
    plt.show()


if __name__ == '__main__':
    args = get_argument()
    path = "output_solutions"
    plot_graphs(path=path, T2=float(args.T2))
