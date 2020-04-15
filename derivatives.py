# Definition of all derivatives function in functions.py
from parameters import *

def Jacobian(x):
    df1 =  np.array([1, 0, 1, 1, 0, 1])
    df2 = np.array([0, 2, 0, 0, 2, 4])
    df3 = np.array([0, 0, 1, 2, 1, 0])
    df4 = np.array([0, 2*K1*x[1], 0, 0, 0, -1])
    df5 = np.array([0, -x[3], K2*x[4], -x[1], K2*x[2], 0])
    df6 = np.array([0, dH_H2, dH_CO, dH_CO2, dH_H2O_k, dH_CH4])
    return np.array([df1, df2, df3, df4, df5, df6])

def main():
    pass

if __name__ == "__main__":
    main()
