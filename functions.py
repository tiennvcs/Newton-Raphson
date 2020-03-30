# Definitions of all funtions of system equations and their derivatives.


def f1(n_1: float, n_2: float, n_3:float, n_4:float, n_5:float, n_6:float):
    f = n_1 + n_2 + n_4 + n6 - 1
    return f

def f2(n_1:float, n_2:float, n_3: float, n_4: float, n_5: float, n_6: float):
    f = 2*n_2 + 2*n_5 + 4*n_6 - a - 2*(w+q)
    return f

def f3(n_1: float, n_2: float, n_3: float, n_4: float, n_5: float, n_6: float):
    f = n_3 + 2*n_4 + n_5 - (b + w + q + 2*m)
    return f

def f4(n_1: float, n_2: float, n_3: float, n_4: float, n_5: float, n_6: float):
    f = K_1 * n_2**2 - n_6
    return f

def f5(n_1: float, n_2: float, n_3: float, n_4: float, n_5: float, n_6: float):
    f = K_2 * n_3*n_5 - n_2*n_4
    return f

def f6(n_1: float, n_2: float, n_3: float, n_4: float, n_5: float, n_6: float):
    f = dH_H2 * n_2 + dH_CO * n_3 + dH_CO2 * n_4 + dH_H20_k * n_5 + dH_CH4 * n_6 + 3.76*m*dH_N2 - dH_trau - w*dH_H2O_l
    return f	
