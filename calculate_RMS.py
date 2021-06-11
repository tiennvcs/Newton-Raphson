import os
import argparse
import numpy as np
from get_values import get_values


def get_argument():
    parser = argparse.ArgumentParser(description="Solve equation system using Newton-Raphson")
    parser.add_argument("-T2", help="Nhiệu độ vừng khử", type=int, default=750.0)   # 750, 800, 850, 900
    return parser.parse_args()


def get_experimental_values(path: str, T2: float):
    experimental_data = {
         'C': [], 
        'H2': [], 
        'CO': [], 
        'CO2': [], 
        'CH4': [],
    }
    for file in os.listdir(path):
        if str(T2).split(".")[0] in file:
            with open(os.path.join(path, file), 'r') as f:
                f.readline()
                for line in f.readlines():
                    values = line.rstrip("\n").split(" ")
                    experimental_data['C'].append(float(values[1]))
                    experimental_data['H2'].append(float(values[2]))
                    experimental_data['CO'].append(float(values[3]))
                    experimental_data['CO2'].append(float(values[4]))
                    experimental_data['CH4'].append(float(values[5]))
    return experimental_data


def get_theory_values(path: str, T2: float):

    _, n1_percents, n2_percents, n3_percents, n4_percents, n6_percents = get_values(path=path, T2=T2)
    return {
        'C': n1_percents, 
        'H2':n2_percents, 
        'CO':n3_percents, 
        'CO2':n4_percents, 
        'CH4':n6_percents,
    }


def caculate_RMS(experimental_data: dict, theory_data: dict):
    RMSE_C = np.sqrt(np.sum(np.square(np.array(theory_data['C']) - np.array(experimental_data['C'])) / len(theory_data['C'])))
    RMSE_H2 = np.sqrt(np.sum(np.square(np.array(theory_data['H2']) - np.array(experimental_data['H2'])) / len(theory_data['H2'])))
    RMSE_CO = np.sqrt(np.sum(np.square(np.array(theory_data['CO']) - np.array(experimental_data['CO'])) / len(theory_data['CO'])))
    RMSE_CO2 = np.sqrt(np.sum(np.square(np.array(theory_data['CO2']) - np.array(experimental_data['CO2'])) / len(theory_data['CO2'])))
    RMSE_CH4 = np.sqrt(np.sum(np.square(np.array(theory_data['CH4']) - np.array(experimental_data['CH4'])) / len(theory_data['CH4'])))
    RMSE_sum =  np.sqrt(((np.mean(theory_data['C'])-np.mean(experimental_data['C']))**2 +\
                (np.mean(theory_data['H2'])-np.mean(experimental_data['H2']))**2 +\
                (np.mean(theory_data['CO'])-np.mean(experimental_data['CO']))**2 +\
                (np.mean(theory_data['CO2'])-np.mean(experimental_data['CO2']))**2 +\
                (np.mean(theory_data['CH4'])-np.mean(experimental_data['CH4']))**2)/5)
                
    return {
        'RMSE_C': RMSE_C,
        'RMSE_H2': RMSE_H2,
        'RMSE_CO': RMSE_CO,
        'RMSE_CO2': RMSE_CO2,
        'RMSE_CH4': RMSE_CH4,
        'RMSE_sum': RMSE_sum,
    }


def main(args):
    path_experiments = "experimental_data"
    path_theory = "running_data"
    experimental_data = get_experimental_values(path_experiments, args.T2)
    theory_data = get_theory_values(path=path_theory, T2=args.T2)
    RMSs = caculate_RMS(experimental_data=experimental_data, theory_data=theory_data)
    print("- The RMSE of C: {}".format(RMSs['RMSE_C']))
    print("- The RMSE of H2: {}".format(RMSs['RMSE_H2']))
    print("- The RMSE of CO: {}".format(RMSs['RMSE_CO']))
    print("- The RMSE of CO2: {}".format(RMSs['RMSE_CO2']))
    print("- The RMSE of CH4: {}".format(RMSs['RMSE_CH4']))
    print("- The Sum RMSE: {}".format(RMSs['RMSE_sum']))


if __name__ == '__main__':
    args = get_argument()
    main(args)
