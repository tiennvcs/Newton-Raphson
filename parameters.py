# Store all parameters of problem
import numpy as np


a = 1.28
b = 0.64
w = 0.145

dH_trau = 365736
dH_H2O_l = -214890 # kJ/kmol
dH_H2O_k = -214890 # kJ/kmol

MC1 = 0.75
q = 137.28 * m * MC1 / 18 / (1-MC1)   # Calculate when have ER
m = ER*(1 + 1.28/4 - 0.64/2)          # Calculate when have ER

exponent1 = 7082.848/T2 + (-6.567)*np.log(T2) + 7.466 * 1e-3 / 2 * T2 + (-2.164*1e-6) / 6 * T2 * T2 + 0.701 * 1e-5 / 2 / T2 / T2 + 32.541
K1 = np.e ** exponent1          # Calculate by (23) fomular

exponent2 = 5870.53/T2 + 1.86*np.log(T2) + 2.7 * 1e-4 * T2 + 58200/T2/T2 + 18.007
K2 = np.e ** exponent2                # Calculate by (24) fomular

dH_H2 =        # Calculate by (14) fomular.
dH_CO = 0       # Calculate by (14) fomular.
dH_CO2 = 0
dH_N2 = 0       # Calculate by (14) fomular.
dH_CH4 = 0      # Calculate by (14) fomular.
