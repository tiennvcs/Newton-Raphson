# Definitions of all funtions of system equations.
from parameters import *


def f1(n1: float, n2: float, n3:float, n4:float, n5:float, n6:float):
    f = n1 + n2 + n4 + n6 - 1
    return f

def f2(n1:float, n2:float, n3: float, n4: float, n5: float, n6: float):
    f = 2*n2 + 2*n5 + 4*n6 - a - 2*(w+q)
    return f

def f3(n1: float, n2: float, n3: float, n4: float, n5: float, n6: float):
    f = n3 + 2*n4 + n5 - (b + w + q + 2*m)
    return f

def f4(n1: float, n2: float, n3: float, n4: float, n5: float, n6: float):
    f = K1 * n2**2 - n6
    return f

def f5(n1: float, n2: float, n3: float, n4: float, n5: float, n6: float):
    f = K2 * n3*n5 - n2*n4
    return f

def f6(n1: float, n2: float, n3: float, n4: float, n5: float, n6: float):
    f = dH_H2 * n2 + dH_CO * n3 + dH_CO2 * n4 + dH_H2O_k * n5 + dH_CH4 * n6 + 3.76*m*dH_N2 - dH_trau - w*dH_H2O_l
    return f

def main(args):
    pass


if __name__ == "__main__":
    main()
