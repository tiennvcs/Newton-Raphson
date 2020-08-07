import os
import argparse
import numpy as np
from get_values import get_values_n1, get_values_n2, get_values_n3, get_values_n4, get_values_n6


def get_argument():
    parser = argparse.ArgumentParser(description="Solve equation system using Newton-Raphson")
    parser.add_argument("-T2", help="Nhiệu độ vừng khử", type=int, default=750.0)   # 750, 800, 850, 900
    return parser.parse_args()


def get_experiental_values(path: str, T2: float):
    ERs = {}
    for file in os.listdir(path):
        if str(T2).split(".")[0] in file:
            with open(os.path.join(path, file), 'r') as f:
                f.readline()
                for line in f.readlines():
                    values = line.rstrip("\n").split(" ")
                    ERs[float(values[0])] = np.round([float(value) for value in values[1:]], 2)
    return ERs

def get_theory_values(path: str, T2: float):
    n1_percents, n1_values = get_values_n1(path, T2)
    n2_percents, n2_values = get_values_n2(path, T2)
    n3_percents, n3_values = get_values_n3(path, T2)
    n4_percents, n4_values = get_values_n4(path, T2)
    n6_percents, n6_values = get_values_n6(path, T2)

    ERs = dict()
    ERs[0.2] = np.round([n1_percents[0], n2_percents[0], n3_percents[0], n4_percents[0], n6_percents[0]], 2)
    ERs[0.25] = np.round([n1_percents[1], n2_percents[1], n3_percents[1], n4_percents[1], n6_percents[1]], 2)
    ERs[0.3] = np.round([n1_percents[2], n2_percents[2], n3_percents[2], n4_percents[2], n6_percents[2]], 2)
    ERs[0.35] = np.round([n1_percents[3], n2_percents[3], n3_percents[3], n4_percents[3], n6_percents[3]], 2)
    ERs[0.4] = np.round([n1_percents[4], n2_percents[4], n3_percents[4], n4_percents[4], n6_percents[4]], 2)

    return ERs

def caculate_RMS(experimental_data: dict, theory_data: dict):
    print(experimental_data)
    print(theory_data)
    RMS_1 = np.sqrt(np.sum(np.square(theory_data[0.2][1:] - experimental_data[0.2][1:]) / len(theory_data[0.2][1:])))
    RMS_2 = np.sqrt(np.sum(np.square(theory_data[0.25][1:] - experimental_data[0.25][1:]) / len(theory_data[0.25][1:])))
    RMS_3 = np.sqrt(np.sum(np.square(theory_data[0.3][1:] - experimental_data[0.3][1:]) / len(theory_data[0.3][1:])))
    RMS_4 = np.sqrt(np.sum(np.square(theory_data[0.35][1:] - experimental_data[0.35][1:]) / len(theory_data[0.35][1:])))
    RMS_5 = np.sqrt(np.sum(np.square(theory_data[0.4][1:] - experimental_data[0.4][1:]) / len(theory_data[0.4][1:])))

    return np.array([RMS_1, RMS_2, RMS_3, RMS_4, RMS_5])


def main(args):
    path_experiments = "experimental_data"
    path_theory = "output_solutions"
    experimental_data = get_experiental_values(path_experiments, args.T2)
    theory_data = get_theory_values(path=path_theory, T2=args.T2)
    RMSs = caculate_RMS(experimental_data=experimental_data, theory_data=theory_data)
    print(RMSs.T)

if __name__ == '__main__':
    args = get_argument()
    main(args)
