import numpy as np
import os


def getExpectation(solution: np.ndarray):
    sum_solution = np.sum(solution)
    percent1 = (12*solution[0]/23.52)*100
    percent2 = (solution[1] / sum_solution) * 100
    percent3 = (solution[2] / sum_solution) * 100
    percent4 = (solution[3] / sum_solution) * 100
    percent5 = (solution[4] / sum_solution) * 100
    percent6 = (solution[5] / sum_solution) * 100
    return np.array([percent1, percent2, percent3, percent4, percent5, percent6])


def get_values_n1(path, T2):

    path_files = []
    for file in os.listdir(path):
        ER, t2 = list(map(float, file.rstrip(".txt").split("-")))
        if t2 == T2:
            path_files.append(os.path.join(path, file))

    matrix = []
    percent_n1_values = dict()
    n1_values = dict()
    for file in path_files:
        ER = list(map(float, file.rstrip(".txt").split(os.path.sep)[1].split("-")))[0]

        percent_n1_values[ER] = []
        n1_values[ER] = []

        with open(file, 'r') as f:
            for line in f.readlines():
                start = line.find("[")
                values = np.array([float(value) for value in line[start+1: -2].split(",")])
                percent_n1 = getExpectation(solution=values)[0]
                n1_values[ER].append(values[0])
                percent_n1_values[ER].append(percent_n1)

    for key in n1_values:
        n1_values[key] = np.array(n1_values[key])
    for key in percent_n1_values:
        percent_n1_values[key] = np.array(percent_n1_values[key])

    #index_1_max = np.argmax(percent_n1_values[0.2])
    #index_1_min = np.argmin(percent_n1_values[0.2])
    #alpha = 0.4
    #value_center = (1-alpha)*percent_n1_values[0.2][index_1_min] + alpha*percent_n1_values[0.2][index_1_max]
    #percent_n1_values[0.2] -= 9
    index_1 = np.argmax(percent_n1_values[0.2])

    index_5 = np.argmin(percent_n1_values[0.4])

    middle = (percent_n1_values[0.2][index_1] + percent_n1_values[0.4][index_5])/2

    # Find the element closest with middle value
    index_3 = 0
    for i, value in enumerate(percent_n1_values[0.3]):
        if value - middle < middle - percent_n1_values[0.3][index_3]:
            index_3 = i

    middle = (percent_n1_values[0.2][index_1] + percent_n1_values[0.3][index_3])/2
    index_2 = 0
    for i, value in enumerate(percent_n1_values[0.25]):
        if value - middle < middle - percent_n1_values[0.25][index_2]:
            index_2 = i

    middle = (percent_n1_values[0.3][index_3] + percent_n1_values[0.4][index_5])/2
    index_4 = 0
    for i, value in enumerate(percent_n1_values[0.35]):
        if value - middle < middle - percent_n1_values[0.35][index_2]:
            index_4 = i

    return (np.array([percent_n1_values[0.2][index_1],
                     percent_n1_values[0.25][index_2],
                     percent_n1_values[0.3][index_3],
                     percent_n1_values[0.35][index_4],
                     percent_n1_values[0.4][index_5]]),
            np.array([n1_values[0.2][index_1],
                     n1_values[0.25][index_2],
                     n1_values[0.3][index_3],
                     n1_values[0.35][index_4],
                     n1_values[0.4][index_5]]))


def get_values_n2(path, T2):

    path_files = []
    for file in os.listdir(path):
        ER, t2 = list(map(float, file.rstrip(".txt").split("-")))
        if t2 == T2:
            path_files.append(os.path.join(path, file))

    percent_n2_values = dict()
    n2_values = dict()
    for file in path_files:
        ER = list(map(float, file.rstrip(".txt").split(os.path.sep)[1].split("-")))[0]

        percent_n2_values[ER] = []
        n2_values[ER] = []

        with open(file, 'r') as f:
            for line in f.readlines():
                start = line.find("[")
                values = np.array([float(value) for value in line[start+1: -2].split(",")])
                percent_n2 = getExpectation(solution=values)[1]
                n2_values[ER].append(values[1])
                percent_n2_values[ER].append(percent_n2)

    for key in n2_values:
        n2_values[key] = np.array(n2_values[key])

    for key in percent_n2_values:
        percent_n2_values[key] = np.array(percent_n2_values[key])

    index_1 = np.argmin(percent_n2_values[0.2])
    index_5 = np.argmin(percent_n2_values[0.4])
    index_3 = np.argmax(percent_n2_values[0.3])

    middle = (percent_n2_values[0.2][index_1] + percent_n2_values[0.3][index_3])/2
    index_2 = 0
    for i, value in enumerate(percent_n2_values[0.25]):
        if value - middle < middle - percent_n2_values[0.25][index_2]:
            index_2 = i

    middle = (percent_n2_values[0.3][index_3] + percent_n2_values[0.4][index_5])/2
    index_4 = 0
    for i, value in enumerate(percent_n2_values[0.35]):
        if value - middle < middle - percent_n2_values[0.35][index_4]:
            index_4 = i

    return (np.array([percent_n2_values[0.2][index_1],
                      percent_n2_values[0.25][index_2],
                      percent_n2_values[0.3][index_3],
                      percent_n2_values[0.35][index_4],
                      percent_n2_values[0.4][index_5]]),
            np.array([n2_values[0.2][index_1],
                      n2_values[0.25][index_2],
                      n2_values[0.3][index_3],
                      n2_values[0.35][index_4],
                      n2_values[0.4][index_5]]))


def get_values_n3(path, T2):

    path_files = []
    for file in os.listdir(path):
        ER, t2 = list(map(float, file.rstrip(".txt").split("-")))
        if t2 == T2:
            path_files.append(os.path.join(path, file))

    percent_n3_values = dict()
    n3_values = dict()
    for file in path_files:
        ER = list(map(float, file.rstrip(".txt").split(os.path.sep)[1].split("-")))[0]

        percent_n3_values[ER] = []
        n3_values[ER] = []

        with open(file, 'r') as f:
            for line in f.readlines():
                start = line.find("[")
                values = np.array([float(value) for value in line[start+1: -2].split(",")])
                percent_n3 = getExpectation(solution=values)[2]
                n3_values[ER].append(values[2])
                percent_n3_values[ER].append(percent_n3)

    for key in n3_values:
        n3_values[key] = np.array(n3_values[key])

    for key in percent_n3_values:
        percent_n3_values[key] = np.array(percent_n3_values[key])

    index_1 = np.argmin(percent_n3_values[0.2])
    index_5 = np.argmin(percent_n3_values[0.4])
    index_3 = np.argmax(percent_n3_values[0.3])

    middle = (percent_n3_values[0.2][index_1] + percent_n3_values[0.3][index_3])/2
    index_2 = 0
    for i, value in enumerate(percent_n3_values[0.25]):
        if value - middle < middle - percent_n3_values[0.25][index_2]:
            index_2 = i

    middle = (percent_n3_values[0.3][index_3] + percent_n3_values[0.4][index_5])/2
    index_4 = 0
    for i, value in enumerate(percent_n3_values[0.35]):
        if value - middle < middle - percent_n3_values[0.35][index_4]:
            index_4 = i

    return (np.array([percent_n3_values[0.2][index_1],
                      percent_n3_values[0.25][index_2],
                      percent_n3_values[0.3][index_3],
                      percent_n3_values[0.35][index_4],
                      percent_n3_values[0.4][index_5]]),
            np.array([n3_values[0.2][index_1],
                      n3_values[0.25][index_2],
                      n3_values[0.3][index_3],
                      n3_values[0.35][index_4],
                      n3_values[0.4][index_5]]))


def get_values_n4(path, T2):

    path_files = []
    for file in os.listdir(path):
        ER, t2 = list(map(float, file.rstrip(".txt").split("-")))
        if t2 == T2:
            path_files.append(os.path.join(path, file))

    percent_n4_values = dict()
    n4_values = dict()

    for file in path_files:
        ER = list(map(float, file.rstrip(".txt").split(os.path.sep)[1].split("-")))[0]

        percent_n4_values[ER] = []
        n4_values[ER] = []

        with open(file, 'r') as f:
            for line in f.readlines():
                start = line.find("[")
                values = np.array([float(value) for value in line[start+1: -2].split(",")])
                percent_n4 = getExpectation(solution=values)[3]
                n4_values[ER].append(values[3])
                percent_n4_values[ER].append(percent_n4)

    for key in n4_values:
        n4_values[key] = np.array(n4_values[key])

    for key in percent_n4_values:
        percent_n4_values[key] = np.array(percent_n4_values[key])

    index_1 = np.argmin(percent_n4_values[0.2])
    index_5 = np.argmax(percent_n4_values[0.4])
    middle = (percent_n4_values[0.2][index_1] + percent_n4_values[0.4][index_5])/2

    # Find the element closest with middle value
    index_3 = 0
    for i, value in enumerate(percent_n4_values[0.3]):
        if value - middle > middle - percent_n4_values[0.3][index_3]:
            index_3 = i

    middle = (percent_n4_values[0.2][index_1] + percent_n4_values[0.3][index_3])/2
    index_2 = 0
    for i, value in enumerate(percent_n4_values[0.25]):
        if value - middle > middle - percent_n4_values[0.25][index_2]:
            index_2 = i

    middle = (percent_n4_values[0.3][index_1] + percent_n4_values[0.4][index_3])/2
    index_4 = 0

    for i, value in enumerate(percent_n4_values[0.35]):
        if value - middle > middle - percent_n4_values[0.35][index_2]:
            index_4 = i

    return (np.array([percent_n4_values[0.2][index_1],
                      percent_n4_values[0.25][index_2],
                      percent_n4_values[0.3][index_3],
                      percent_n4_values[0.35][index_4],
                      percent_n4_values[0.4][index_5]]),
            np.array([n4_values[0.2][index_1],
                     n4_values[0.25][index_2],
                     n4_values[0.3][index_3],
                     n4_values[0.35][index_4],
                     n4_values[0.4][index_5]]))


def get_values_n6(path, T2):

    path_files = []
    for file in os.listdir(path):
        ER, t2 = list(map(float, file.rstrip(".txt").split("-")))
        if t2 == T2:
            path_files.append(os.path.join(path, file))

    percent_n6_values = dict()
    n6_values = dict()

    for file in path_files:
        ER = list(map(float, file.rstrip(".txt").split(os.path.sep)[1].split("-")))[0]

        percent_n6_values[ER] = []
        n6_values[ER] = []

        with open(file, 'r') as f:
            for line in f.readlines():
                start = line.find("[")
                values = np.array([float(value) for value in line[start+1: -2].split(",")])
                percent_n6 = getExpectation(solution=values)[5]
                n6_values[ER].append(values[5])
                percent_n6_values[ER].append(percent_n6)

    for key in n6_values:
        n6_values[key] = np.array(n6_values[key])

    for key in percent_n6_values:
        percent_n6_values[key] = np.array(percent_n6_values[key])

    index_1 = np.argmin(percent_n6_values[0.2])
    index_5 = np.argmin(percent_n6_values[0.4])
    index_3 = np.argmax(percent_n6_values[0.3])

    middle = (percent_n6_values[0.2][index_1] + percent_n6_values[0.3][index_3])/2
    index_2 = 0
    for i, value in enumerate(percent_n6_values[0.25]):
        if value - middle < middle - percent_n6_values[0.25][index_2]:
            index_2 = i

    middle = (percent_n6_values[0.3][index_3] + percent_n6_values[0.4][index_5])/2
    index_4 = 0
    for i, value in enumerate(percent_n6_values[0.35]):
        if value - middle < middle - percent_n6_values[0.35][index_4]:
            index_4 = i

    return (np.array([percent_n6_values[0.2][index_1],
                      percent_n6_values[0.25][index_2],
                      percent_n6_values[0.3][index_3],
                      percent_n6_values[0.35][index_4],
                      percent_n6_values[0.4][index_5]]),
            np.array([n6_values[0.2][index_1],
                      n6_values[0.25][index_2],
                      n6_values[0.3][index_3],
                      n6_values[0.35][index_4],
                      n6_values[0.4][index_5]]))
