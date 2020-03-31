# Definition of all derivatives function in functions.py
from parameters import *

def derivF_1(n1: float, n2:float, n3: float, n4: float, n5: float, n6: float):
    """
    @arguments:
        - n_i (float) the variables of function
    @return value:
        - An array whose elements is derivate of function.
    @note:
        - The derivate of multivariable function is an vector.
    """

    # derf_n_i is giá trị đạo hàm riêng theo biến n_i của hàm số.
    derf_n1 = 1
    derf_n2 = 0
    derf_n3 = 1
    derf_n4 = 1
    derf_n5 = 0
    derf_n6 = 1
    return np.array([derf_n1, derf_n2, derf_n3, derf_n4, derf_n5, derf_n6])

def derivF_2(n1: float, n2:float, n3: float, n4: float, n5: float, n6: float):
    """
    @arguments:
        - n_i (float) the variables of function
    @return value:
        - An array whose elements is derivate of function.
    @note:
        - The derivate of multivariable function is an vector.
    """

    # derf_n_i is giá trị đạo hàm riêng theo biến n_i của hàm số.
    derf_n1 = 0
    derf_n2 = 2
    derf_n3 = 0
    derf_n4 = 0
    derf_n5 = 2
    derf_n6 = 4
    return np.array([derf_n1, derf_n2, derf_n3, derf_n4, derf_n5, derf_n6])

def derivF_3(n1: float, n2:float, n3: float, n4: float, n5: float, n6: float):
    """
    @arguments:
        - n_i (float) the variables of function
    @return value:
        - An array whose elements is derivate of function.
    @note:
        - The derivate of multivariable function is an vector.
    """

    # derf_n_i is giá trị đạo hàm riêng theo biến n_i của hàm số.
    derf_n1 = 0
    derf_n2 = 0
    derf_n3 = 1
    derf_n4 = 2
    derf_n5 = 1
    derf_n6 = 0
    return np.array([derf_n1, derf_n2, derf_n3, derf_n4, derf_n5, derf_n6])


def derivF_4(n1: float, n2:float, n3: float, n4: float, n5: float, n6: float):
    """
    @arguments:
        - n_i (float) the variables of function
    @return value:
        - An array whose elements is derivate of function.
    @note:
        - The derivate of multivariable function is an vector.
    """

    # derf_n_i is giá trị đạo hàm riêng theo biến n_i của hàm số.
    derf_n1 = 0
    derf_n2 = 2 * K1
    derf_n3 = 0
    derf_n4 = 0
    derf_n5 = 0
    derf_n6 = -1
    return np.array([derf_n1, derf_n2, derf_n3, derf_n4, derf_n5, derf_n6])

def derivF_5(n1: float, n2:float, n3: float, n4: float, n5: float, n6: float):
    """
    @arguments:
        - n_i (float) the variables of function
    @return value:
        - An array whose elements is derivate of function.
    @note:
        - The derivate of multivariable function is an vector.
    """

    # derf_n_i is giá trị đạo hàm riêng theo biến n_i của hàm số.
    derf_n1 = 0
    derf_n2 = -n4
    derf_n3 = K2 * n5
    derf_n4 = -n2
    derf_n5 = K2 * n3
    derf_n6 = 0
    return np.array([derf_n1, derf_n2, derf_n3, derf_n4, derf_n5, derf_n6])

def derivF_6(n1: float, n2:float, n3: float, n4: float, n5: float, n6: float):
    """
    @arguments:
        - n_i (float) the variables of function
    @return value:
        - An array whose elements is derivate of function.
    @note:
        - The derivate of multivariable function is an vector.
    """

    # derf_n_i is giá trị đạo hàm riêng theo biến n_i của hàm số.
    derf_n1 = 0
    derf_n2 = dH_H2
    derf_n3 = dH_CO
    derf_n4 = dH_CO2
    derf_n5 = dH_H2O_k
    derf_n6 = dH_CH4
    return np.array([derf_n1, derf_n2, derf_n3, derf_n4, derf_n5, derf_n6])


def main():
    pass


if __name__ == "__main__":
    main()
