import os
import argparse
import numpy as np
from get_values import get_values


def get_argument():
    parser = argparse.ArgumentParser(description="Solve equation system using Newton-Raphson")
    parser.add_argument("-T2", help="Nhiệu độ vừng khử", type=int, default=750.0)   # 750, 800, 850, 900
    return parser.parse_args()


def get_experimental_values(path: str, T2: float):
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

    _, n1_percents, n2_percents, n3_percents, n4_percents, n6_percents = get_values(path=path, T2=T2)

    ERs = dict()
    ERs[0.2] = np.round([n1_percents[0], n2_percents[0], n3_percents[0], n4_percents[0], n6_percents[0]], 2)
    ERs[0.25] = np.round([n1_percents[1], n2_percents[1], n3_percents[1], n4_percents[1], n6_percents[1]], 2)
    ERs[0.3] = np.round([n1_percents[2], n2_percents[2], n3_percents[2], n4_percents[2], n6_percents[2]], 2)
    ERs[0.35] = np.round([n1_percents[3], n2_percents[3], n3_percents[3], n4_percents[3], n6_percents[3]], 2)
    ERs[0.4] = np.round([n1_percents[4], n2_percents[4], n3_percents[4], n4_percents[4], n6_percents[4]], 2)

    return ERs

def caculate_RMS(experimental_data: dict, theory_data: dict):
    RMS_1 = np.sqrt(np.sum(np.square(theory_data[0.2] - experimental_data[0.2]) / len(theory_data[0.2])))
    RMS_2 = np.sqrt(np.sum(np.square(theory_data[0.25] - experimental_data[0.25]) / len(theory_data[0.25])))
    RMS_3 = np.sqrt(np.sum(np.square(theory_data[0.3] - experimental_data[0.3]) / len(theory_data[0.3])))
    RMS_4 = np.sqrt(np.sum(np.square(theory_data[0.35] - experimental_data[0.35]) / len(theory_data[0.35])))
    RMS_5 = np.sqrt(np.sum(np.square(theory_data[0.4] - experimental_data[0.4]) / len(theory_data[0.4])))

    return np.array([RMS_1, RMS_2, RMS_3, RMS_4, RMS_5])


def main(args):
    path_experiments = "experimental_data"
    path_theory = "running_data"
    experimental_data = get_experimental_values(path_experiments, args.T2)
    theory_data = get_theory_values(path=path_theory, T2=args.T2)
    RMSs = caculate_RMS(experimental_data=experimental_data, theory_data=theory_data)
    print(RMSs.T)

if __name__ == '__main__':
    args = get_argument()
    main(args)
