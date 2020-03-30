# Definition of all derivatives function in functions.py

def derivF_1(n_1: float, n_2:float, n_3: float, n_4: float, n_5: float, n_6: float):
    """
    @arguments:
        - n_i (float) the variables of function
    @return value:
        - An array whose elements is derivate of function.
    @note:
        - The derivate of multivariable function is an vector.
    """

    # derf_n_i is giá trị đạo hàm riêng theo biến n_i của hàm số.
    derf_n_1 = 1
    derf_n_2 = 0
    derf_n_3 = 1
    derf_n_4 = 1
    derf_n_5 = 0
    derf_n_6 = 1
    return [derf_n_1, derf_n_2, derf_n_3, derf_n_4, derf_n_5, derf_n_6]

def derivF_2(n_1: float, n_2:float, n_3: float, n_4: float, n_5: float, n_6: float):
    """
    @arguments:
        - n_i (float) the variables of function
    @return value:
        - An array whose elements is derivate of function.
    @note:
        - The derivate of multivariable function is an vector.
    """

    # derf_n_i is giá trị đạo hàm riêng theo biến n_i của hàm số.
    derf_n_1 = 0
    derf_n_2 = 2
    derf_n_3 = 0
    derf_n_4 = 0
    derf_n_5 = 2
    derf_n_6 = 4
    return [derf_n_1, derf_n_2, derf_n_3, derf_n_4, derf_n_5, derf_n_6]

def derivF_3(n_1: float, n_2:float, n_3: float, n_4: float, n_5: float, n_6: float):
    """
    @arguments:
        - n_i (float) the variables of function
    @return value:
        - An array whose elements is derivate of function.
    @note:
        - The derivate of multivariable function is an vector.
    """

    # derf_n_i is giá trị đạo hàm riêng theo biến n_i của hàm số.
    derf_n_1 = 0
    derf_n_2 = 0
    derf_n_3 = 1
    derf_n_4 = 2
    derf_n_5 = 1
    derf_n_6 = 0
    return [derf_n_1, derf_n_2, derf_n_3, derf_n_4, derf_n_5, derf_n_6]


def derivF_4(n_1: float, n_2:float, n_3: float, n_4: float, n_5: float, n_6: float):
    """
    @arguments:
        - n_i (float) the variables of function
    @return value:
        - An array whose elements is derivate of function.
    @note:
        - The derivate of multivariable function is an vector.
    """

    # derf_n_i is giá trị đạo hàm riêng theo biến n_i của hàm số.
    derf_n_1 = 0
    derf_n_2 = 2 * K1
    derf_n_3 = 0
    derf_n_4 = 0
    derf_n_5 = 0
    derf_n_6 = -1
    return [derf_n_1, derf_n_2, derf_n_3, derf_n_4, derf_n_5, derf_n_6]

def derivF_5(n_1: float, n_2:float, n_3: float, n_4: float, n_5: float, n_6: float):
    """
    @arguments:
        - n_i (float) the variables of function
    @return value:
        - An array whose elements is derivate of function.
    @note:
        - The derivate of multivariable function is an vector.
    """

    # derf_n_i is giá trị đạo hàm riêng theo biến n_i của hàm số.
    derf_n_1 = 0
    derf_n_2 = -n_4
    derf_n_3 = K2 * n_5
    derf_n_4 = -n_2
    derf_n_5 = K2 * n_3
    derf_n_6 = 0
    return [derf_n_1, derf_n_2, derf_n_3, derf_n_4, derf_n_5, derf_n_6]

def derivF_6(n_1: float, n_2:float, n_3: float, n_4: float, n_5: float, n_6: float):
    """
    @arguments:
        - n_i (float) the variables of function
    @return value:
        - An array whose elements is derivate of function.
    @note:
        - The derivate of multivariable function is an vector.
    """

    # derf_n_i is giá trị đạo hàm riêng theo biến n_i của hàm số.
    derf_n_1 = 0
    derf_n_2 = dH_H2
    derf_n_3 = dH_CO
    derf_n_4 = dH_CO2
    derf_n_5 = dh_H2O_k
    derf_n_6 = dH_CH4
    return [derf_n_1, derf_n_2, derf_n_3, derf_n_4, derf_n_5, derf_n_6]
