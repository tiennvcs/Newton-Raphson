# Definitions of all funtions of system equations.
from parameters import *

def F(x):
    f1 = x[0] + x[2] + x[3] + x[5] - 1
    f2 = 2*x[1] + 2*x[4] + 4*x[5] - a - 2*(w+q)
    f3 = x[2] + 2*x[3] + x[4] - (b + w + q + 2*m)
    f4 = K1 * x[1]**2 - x[5]
    f5 = K2 * x[2]*x[4] - x[1]*x[3]
    f6 = dH_H2 * x[1] + dH_CO * x[2] + dH_CO2 * x[3] + dH_H2O_k * x[4] + dH_CH4 * x[5] + 3.76*m*dH_N2 - dH_trau - w*dH_H2O_l
    return np.array([f1, f2, f3, f4, f5, f6])

def main(args):
    pass

if __name__ == "__main__":
    main()
