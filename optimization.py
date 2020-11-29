import numpy as np
import argparse
from get_experimental_values import get_values_n1
from regression_experimental import get_LHV

def yOut(f1, f2, alpha):
    return alpha*f1 + (1-alpha)*f2


def load_data():

    _, yC = get_values_n1(path='experimental_data')
    _, yLHV = get_LHV('./experimental_data/LowHitValues.txt')
    return (yC, yLHV)


def optimize(ERs, T2s, alpha):
    
    X = []
    ER_T2s = []

    yC, yLHV = load_data()
    
    print(yC)

    i = 0
    for T2 in T2s:
        for ER in ERs:
        
            ER_T2s.append([ER, T2])
            X.append(np.array([yC[i], yLHV[i]]))

            i += 1

    X = np.array(X)
    print(np.min(X, axis=0))
    print(np.max(X, axis=0))
    #print(X)
    normalize_X = (X-np.min(X, axis=0)+1)/(np.max(X, axis=0)-np.min(X, axis=0))
    
    Youts = []
    for pair in normalize_X:
        yout = yOut(f1=pair[0], f2=pair[1], alpha=alpha)
        Youts.append(yout)

    print("\n"*2)
    print("-"*27 + "CALCULATING C AND LHV VALUE WITH ALPHA = {}".format(alpha) + "-"*27)
    print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^20}|{:^20}|{:^10}|".format(
        'T2', 'ER', '%C', 'LHV', 'normalized %C', 'normalized LHV', 'Y_balance'))
    print("-"*98)
    
    i = 0
    for T2 in T2s:
        for ER in ERs:
            print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^20}|{:^20}|{:^10}|".format(
                       T2, ER, np.round(X[i][0], 3), np.round(X[i][1], 3), 
                       np.round(normalize_X[i][0], 3), np.round(normalize_X[i][1], 3), np.round(Youts[i], 3)))
    
            i += 1
        print("-"*98)
    print("-"*98)

    Youts = np.array(Youts)
    best_index = np.argmax(Youts)

    print("---> The best coeficient (ER, T2) to maximize C and LHV (with alpha = {}) is {}".format(alpha, ER_T2s[best_index]))
    print("---> The value of C and LHV when ER = {} and T2 = {} (with alpha = {}) is {}".format(
        ER_T2s[best_index][0], ER_T2s[best_index][1], alpha, Youts[best_index]))

    return normalize_X, Youts, best_index


def main(args):
    
    T2s = [750, 800, 850, 900]
    ERs = [0.2, 0.25, 0.3, 0.35, 0.4]
    
    optimize(ERs=ERs, T2s=T2s, alpha=args['alpha'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Optimize two objective functions')
    parser.add_argument('--alpha', '-a', default=0.5, type=float, 
                        help='The alpha coeficient')
    args = vars(parser.parse_args())

    main(args)