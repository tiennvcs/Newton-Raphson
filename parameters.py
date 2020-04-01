# Store all parameters of problem
import numpy as np
from constants import *

ER = 0.25
T2 = 750 + 273.15

m = ER * (1 + 1.28/4 - 0.64/2)        # Calculate when have ER
q = 137.28 * m * MC1 / 18 / (1-MC1)   # Calculate when have ER

exponent1 = 7082.848/T2 + (-6.567)*np.log(T2) + 7.466 * 1e-3 / 2 * T2 + (-2.164*1e-6) / 6 * T2 * T2 + 0.701 * 1e-5 / 2 / T2 / T2 + 32.541
K1 = np.e ** exponent1                # Calculate by (23) fomular

exponent2 = 5870.53/T2 + 1.86*np.log(T2) + 2.7 * 1e-4 * T2 + 58200/T2/T2 + 18.007
K2 = np.e ** exponent2                # Calculate by (24) fomular

dentaT = T2 - T1

T_am = (T1+T2)/2

C_p_H2 = R*(A_H2 + B_H2 + C_H2/3*(4*T_am**2-T1*T2)+D_H2/T1/T2)
C_p_CO = R*(A_CO + B_CO + C_CO/3*(4*T_am**2-T1*T2)+D_CO/T1/T2)
C_p_CO2 = R*(A_CO2 + B_CO2 + C_CO2/3*(4*T_am**2-T1*T2)+D_CO2/T1/T2)
C_p_N2 = R*(A_N2 + B_N2 + C_N2/3*(4*T_am**2-T1*T2)+D_N2/T1/T2)
C_p_CH4 = R*(A_CH4 + B_CH4 + C_CH4/3*(4*T_am**2-T1*T2)+D_CH4/T1/T2)

dentaH_H2 = dentaT * C_p_H2
dentaH_CO = dentaT * C_p_CO
dentaH_CO2 = dentaT * C_p_CO2
dentaH_N2 = dentaT * C_p_N2
dentaH_CH4 = dentaT * C_p_CH4

dH_H2 = H_f_H2 + dentaH_H2      # Calculate by (14) fomular.
dH_CO = H_f_CO + dentaH_CO       # Calculate by (14) fomular.
dH_CO2 = H_f_CO2 + dentaH_CO2
dH_N2 = H_f_N2 + dentaH_N2       # Calculate by (14) fomular.
dH_CH4 = H_f_CH4 + dentaH_CH4      # Calculate by (14) fomular.
