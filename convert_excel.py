import os
import argparse
import numpy as np
import pandas as pd

def get_argument():
    parser = argparse.ArgumentParser(description="Solve equation system using Newton-Raphson")
    parser.add_argument("-ER", help="Hệ số không khí cấp", type=float, default=0.2) # 0.25, 0.3, 0.35, 0.4
    parser.add_argument("-T2", help="Nhiệu độ vừng khử", type=int, default=750)   # 750, 800, 850, 900
    args = parser.parse_args()
    return args

def read_data(path):
    matrix = []
    with open(path, 'r') as f:
        for line in f.readlines():
            n = int(line.split(" ")[0])
            start = line.find("[")
            values = np.array([round(float(value),3) for value in line[start+1: -2].split(",")])
            matrix.append(np.append(n, values))

    return matrix


def main(args):
    ER = float(args.ER)
    T2 = float(args.T2)
    input_path = os.path.join("output_solutions", "{ER}-{T2}.txt".format(ER=ER, T2=T2))
    data = read_data(input_path)

    output_file = os.path.join("csv_files", "{ER}-{T2}.csv".format(ER=ER, T2=T2))
    data = pd.DataFrame(data, columns = ["Step", "C", "H2", "CO", "CO2", "H20", "CH4"])
    data.to_csv(output_file, sep=",")


if __name__ == "__main__":
    args = get_argument()
    main(args)
