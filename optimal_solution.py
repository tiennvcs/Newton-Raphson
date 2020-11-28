import numpy as np
import argparse


def yC(ER, T2):
    return -0.0621*T2 - 12.749*ER + 88.407

def yLHV(ER, T2):
    return -2.784*T2 + 17319.514*ER + 0.003*T2**2 - 3.18*T2*ER - 25142.857*ER**2 - 583.95

def yOut(f1, f2, alpha):
    return alpha*f1 + (1-alpha)*f2


def optimize(ERs, T2s, f1, f2, alpha):
    
    X = []
    ER_T2s = []

    for T2 in T2s:
        for ER in ERs:
            yc = f1(ER=ER, T2=T2)
            ylhv = f2(ER=ER, T2=T2)
            
            ER_T2s.append([ER, T2])
            X.append(np.array([yc, ylhv]))

    X = np.array(X)
    normalize_X = (X - np.min(X, axis=0))/(np.max(X, axis=0)-np.min(X, axis=0))
    
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
                       T2, ER, np.round(X[i][0], 2), np.round(X[i][1], 2), 
                       np.round(normalize_X[i][0], 2), np.round(normalize_X[i][1], 2), np.round(Youts[i], 2)))
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
    
    #ERs = np.arange(0.2, 0.401, 0.05*args['number_points']/5)
    #T2s = np.arange(750, 901, int(50*args['number_points']/4))
    T2s = np.arange(750, 901, 50)
    ERs = np.round(np.arange(0.2, 0.401, 0.05), 2)

    optimize(ERs=ERs, T2s=T2s, f1=yC, f2=yLHV, alpha=args['alpha'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Optimize two objective functions')
    parser.add_argument('--alpha', '-a', default=0.5, type=float, 
                        help='The alpha coeficient')
    parser.add_argument('--number_points', '-n_points', default=5, 
                        type=int, help='The alpha coeficient')
    args = vars(parser.parse_args())

    main(args)