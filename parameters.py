# Store all parameters of problem
import numpy as np
import sys
from constants import *

if len(sys.argv) == 1:
	ER, T2 = 0.2, 750 + 273.15
elif len(sys.argv) == 3:
	ER = float(sys.argv[2])
	T2 = 750 + 273.15
elif len(sys.argv) >= 5:
	print(sys.argv)
	ER, T2 = float(sys.argv[2]), float(sys.argv[4]) + 273.15

m = ER * (1 + a/4 - b/2)        # Calculate when have ER
q = 4.76 * m / 45.5             # Calculate when have ER

exponent1 = 7082.848/T2 + (-6.567)*np.log(T2) + 7.466 * 1e-3 / 2 * T2 + (-2.164*1e-6) / 6 * T2 * T2 + 0.701 * 1e-5 / 2 / T2 / T2 + 32.541
K1 = np.e ** exponent1                # Calculate by (23) fomular

exponent2 = 5870.53/T2 + 1.86*np.log(T2) + 2.7 * 1e-4 * T2 + 58200/T2/T2 + 18.007
K2 = np.e ** exponent2                # Calculate by (24) fomular

dentaT = T2 - T1

T_am = (T1+T2)/2

Cp_H2 = R*(A_H2 + B_H2*T_am + C_H2/3*(4*T_am**2-T1*T2)+D_H2/T1/T2)
Cp_CO = R*(A_CO + B_CO*T_am + C_CO/3*(4*T_am**2-T1*T2)+D_CO/T1/T2)
Cp_CO2 = R*(A_CO2 + B_CO2*T_am + C_CO2/3*(4*T_am**2-T1*T2)+D_CO2/T1/T2)
Cp_N2 = R*(A_N2 + B_N2*T_am + C_N2/3*(4*T_am**2-T1*T2)+D_N2/T1/T2)
Cp_CH4 = R*(A_CH4 + B_CH4*T_am + C_CH4/3*(4*T_am**2-T1*T2)+D_CH4/T1/T2)

dentaH_H2 = dentaT * Cp_H2
dentaH_CO = dentaT * Cp_CO
dentaH_CO2 = dentaT * Cp_CO2
dentaH_N2 = dentaT * Cp_N2
dentaH_CH4 = dentaT * Cp_CH4

dH_H2 = Hf_H2 + dentaH_H2       # Calculate by (14) fomular.
dH_CO = Hf_CO + dentaH_CO       # Calculate by (14) fomular.
dH_CO2 = Hf_CO2 + dentaH_CO2    # Calculate by (14) fomular.
dH_N2 = Hf_N2 + dentaH_N2       # Calculate by (14) fomular.
dH_CH4 = Hf_CH4 + dentaH_CH4    # Calculate by (14) fomular.

A = a + 2*(w+q)
B = (b+w+q+2*m)
C = dH_trau + w*dH_H2O_l - A*dH_H2/2 - B*dH_CO - 3.76*m*dH_N2