import numpy as np
import os
import argparse
import matplotlib.pyplot as plt
from main import getExpectation

def get_argument():
    parser = argparse.ArgumentParser(description="Solve equation system using Newton-Raphson")
    parser.add_argument("-T2", help="Nhiệu độ vừng khử", type=int, default=750.0)   # 750, 800, 850, 900
    return parser.parse_args()


def get_values(path, T2):
    path_files = []
    for file in os.listdir(path):
        ER, t2 = list(map(float, file.rstrip(".txt").split("-")))
        if t2 == T2:
            path_files.append(os.path.join(path, file))

    matrix = []
    for file in path_files:
        with open(file, 'r') as f:
            #f.readline()
            for line in f.readlines():
                start = line.find("[")
                values = np.array([float(value) for value in line[start+1: -2].split(",")])
                percents = getExpectation(solution=values)
                matrix.append(percents)
                # Just get the first line
                break
    matrix = np.array(matrix)

    return matrix


def plot_graphs(matrix: np.ndarray, T2: float):
    ER = np.array([0.2, 0.25, 0.3, 0.35, 0.4])
    fig, axes = plt.subplots(figsize=(9, 6))
    # print(matrix[:, 0])
    # expected_1 = getExpectation(solution=matrix[:, 0])
    axes.plot(ER, matrix[:, 0], label='% C')
    axes.plot(ER, matrix[:, 1], label='% H_2')
    axes.plot(ER, matrix[:, 2], label='% CO')
    axes.plot(ER, matrix[:, 3], label='% CO_2')
    axes.plot(ER, matrix[:, 4], label='% CH_4')

    axes.set_xlabel("ER", fontsize=14)
    axes.set_ylabel("%", fontsize=14)
    axes.set_xticks(ER)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    args = get_argument()
    path = "output_solutions"
    matrix = get_values(path, T2=float(args.T2))
    plot_graphs(matrix, T2=float(args.T2))
