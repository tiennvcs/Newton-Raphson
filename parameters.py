# Store all parameters of problem

def update(ER: float, T2: float):
    a = 1.28
    b = 0.64
    w = 0.145

    dH_trau = 365736
    dH_H20_l = -214890 # kJ/kmol
    dH_H20_k = -214890 # kJ/kmol

    q = 0           # Calculate when have ER
    m = 0           # Calculate when have ER
    K1 = 0          # Calculate by (23) fomular
    K2 = 0          # Calculate by (24) fomular
    dH_H2 = 0       # Calculate by (14) fomular.
    dH_CO = 0       # Calculate by (14) fomular.
    dH_N2 = 0       # Calculate by (14) fomular.
    dH_CH4 = 0      # Calculate by (14) fomular.
