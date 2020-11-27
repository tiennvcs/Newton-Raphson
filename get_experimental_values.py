import numpy as np
import os

def calculate_LHV(x: np.array):
    LHV_CH4 = 35.88
    LHV_CO = 12.63
    LHV_H2 = 10.78

    LHV_gas = x[5]*LHV_CH4 + x[1]*LHV_H2 + x[2]*LHV_CO
    return LHV_gas*238


def getExpectation(solution: np.ndarray, rounded=2):
    sum_solution = np.sum(solution)
    percent1 = round((12*solution[0]/23.52)*100, rounded)
    percent2 = round((solution[1] / sum_solution) * 100,  rounded)
    percent3 = round((solution[2] / sum_solution) * 100, rounded)
    percent4 = round((solution[3] / sum_solution) * 100, rounded)
    percent5 = round((solution[4] / sum_solution) * 100, rounded)
    percent6 = round((solution[5] / sum_solution) * 100, rounded)
    return np.array([percent1, percent2, percent3, percent4, percent5, percent6])


def get_values(path, T2):

    path_files = []
    for file in os.listdir(path):

        ER, t2 = list(map(float, file.rstrip(".txt").split("-")))
        if t2 == T2:
            path_files.append(os.path.join(path, file))

    n1_values = dict()
    n2_values = dict()
    n3_values = dict()
    n4_values = dict()
    n5_values = dict()
    n6_values = dict()
    average_values = dict()
    expectations = dict()
    n1_expectation = []
    n2_expectation = []
    n3_expectation = []
    n4_expectation = []
    n5_expectation = []
    n6_expectation = []
    LHVs = []

    for file in path_files:

        ER = list(map(float, file.rstrip(".txt").split(os.path.sep)[1].split("-")))[0]

        n1_values[ER] = []
        n2_values[ER] = []
        n3_values[ER] = []
        n4_values[ER] = []
        n5_values[ER] = []
        n6_values[ER] = []

        with open(file, 'r') as f:
            for line in f.readlines():

                values = np.array([float(value) for value in line.split()[1:]])

                n1_values[ER].append(values[0])
                n2_values[ER].append(values[1])
                n3_values[ER].append(values[2])
                n4_values[ER].append(values[3])
                n5_values[ER].append(values[4])
                n6_values[ER].append(values[5])

        average_values[ER] = np.array([
            np.mean(n1_values[ER]),
            np.mean(n2_values[ER]),
            np.mean(n3_values[ER]),
            np.mean(n4_values[ER]),
            np.mean(n5_values[ER]),
            np.mean(n6_values[ER])
        ])

        expectations[ER] = getExpectation(solution=average_values[ER])
        n1_expectation.append(expectations[ER][0])
        n2_expectation.append(expectations[ER][1])
        n3_expectation.append(expectations[ER][2])
        n4_expectation.append(expectations[ER][3])
        n5_expectation.append(expectations[ER][4])
        n6_expectation.append(expectations[ER][5])

        lhv = calculate_LHV(average_values[ER]/np.sum(average_values[ER]))
        LHVs.append(lhv)

    return (LHVs, n1_expectation, n2_expectation, n3_expectation, n4_expectation, n6_expectation)


def get_values_n1(path):


    path_files = []
    ER_T2_values = []
    return_values = []

    for file in os.listdir(path):
        if file == 'LowHitValues.txt':
            continue
        T2 = file.rstrip(".txt")
        with open(os.path.join(path, file), 'r') as f:
            f.readline()
            for line in f.readlines():
                line = line.rstrip().split()
                ER = float(line[0])
                n1 = float(line[1])
                ER_T2_values.append(np.array([T2, ER], dtype=np.float32))
                return_values.append(n1)

    return (ER_T2_values, return_values)


def get_values_n2(path):


    path_files = []
    ER_T2_values = []
    return_values = []

    for file in os.listdir(path):
        if file == 'LowHitValues.txt':
            continue
        T2 = file.rstrip(".txt")
        with open(os.path.join(path, file), 'r') as f:
            f.readline()
            for line in f.readlines():
                line = line.rstrip().split()
                ER = float(line[0])
                n2 = float(line[2])
                ER_T2_values.append(np.array([T2, ER], dtype=np.float32))
                return_values.append(n2)

    return (ER_T2_values, return_values)


def get_values_n3(path):


    path_files = []
    ER_T2_values = []
    return_values = []

    for file in os.listdir(path):
        if file == 'LowHitValues.txt':
            continue
        T2 = file.rstrip(".txt")
        with open(os.path.join(path, file), 'r') as f:
            f.readline()
            for line in f.readlines():
                line = line.rstrip().split()
                ER = float(line[0])
                n3 = float(line[3])
                ER_T2_values.append(np.array([T2, ER], dtype=np.float32))
                return_values.append(n3)

    return (ER_T2_values, return_values)


def get_values_n4(path):


    path_files = []
    ER_T2_values = []
    return_values = []

    for file in os.listdir(path):
        if file == 'LowHitValues.txt':
            continue
        T2 = file.rstrip(".txt")
        with open(os.path.join(path, file), 'r') as f:
            f.readline()
            for line in f.readlines():
                line = line.rstrip().split()
                ER = float(line[0])
                n4 = float(line[4])
                ER_T2_values.append(np.array([T2, ER], dtype=np.float32))
                return_values.append(n4)

    return (ER_T2_values, return_values)


def get_values_n6(path):


    path_files = []
    ER_T2_values = []
    return_values = []

    for file in os.listdir(path):
        if file == 'LowHitValues.txt':
            continue
        T2 = file.rstrip(".txt")
        with open(os.path.join(path, file), 'r') as f:
            f.readline()
            for line in f.readlines():
                line = line.rstrip().split()
                ER = float(line[0])
                n6 = float(line[5])
                ER_T2_values.append(np.array([T2, ER], dtype=np.float32))
                return_values.append(n6)

    return (ER_T2_values, return_values)
