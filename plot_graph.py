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
    (n2_percents, n2_values) = get_values_n2(path, T2)
    (n3_percents, n3_values) = get_values_n3(path, T2)
    (n4_percents, n4_values) = get_values_n4(path, T2)
    (n6_percents, n6_values) = get_values_n6(path, T2)

    ER = np.array([0.2, 0.25, 0.3, 0.35, 0.4])
    fig, axes = plt.subplots(figsize=(6, 4))
    # print(matrix[:, 0])
    # expected_1 = getExpectation(solution=matrix[:, 0])
    axes.plot(ER, n1_percents, 'r', label='% C')
    axes.plot(ER, n2_percents, 'g--', label='% H_2')
    axes.plot(ER, n3_percents, 'c', label='% CO')
    axes.plot(ER, n4_percents, 'b', label='% CO_2')
    axes.plot(ER, n6_percents, 'y', label='% CH_4')

    axes.scatter(ER, n1_percents)
    axes.scatter(ER, n2_percents)
    axes.scatter(ER, n3_percents)
    axes.scatter(ER, n4_percents)
    axes.scatter(ER, n6_percents)


    axes.set_xlabel("ER", fontsize=14)
    axes.set_ylabel("Syngas Compositions (%)", fontsize=14)
    axes.set_xticks(ER)
    axes.set_title(str(T2) + r"$^{0} C$", fontsize=16)
    plt.legend(loc='best')
    plt.show()


if __name__ == '__main__':
    args = get_argument()
    path = "output_solutions"
    plot_graphs(path=path, T2=float(args.T2))
