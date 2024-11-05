import numpy as np

def solubility(P, T, f_300F, f_200F, f_100F):
    sol_300F = f_300F(P)
    sol_200F = f_200F(P)
    sol_100F = f_100F(P)
    if (T < 100) or (T >300):
        print('not available temperature!') 
        return np.nan
    elif (100<=T) and (T<200):
        slope = (sol_200F-sol_100F)/100
        sol = sol_100F + slope*(T-100)
        return sol
    elif (200<=T) and (T<=300):
        slope = (sol_300F-sol_200F)/100
        sol = sol_200F + slope*(T-200)
        return sol

