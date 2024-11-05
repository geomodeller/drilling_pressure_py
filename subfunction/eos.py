from math import exp
from numpy import real

def calculate_z_factor(p, temp, r_g = 0.554):

    a_1 = 0.317842
    a_2 = 0.382216
    a_3 = -7.768354
    a_4 = 14.290531
    a_5 = 0.000002 
    a_6 = -0.004693
    a_7 = 0.096254
    a_8 = 0.166720
    a_9 = 0.966910
    a_10 = 0.063069
    a_11 = -1.966847
    a_12 = 21.0581
    a_13 = -27.0246
    a_14 = 16.23
    a_15 = 207.783 
    a_16 = -488.161
    a_17 = 176.29
    a_18 = 1.88453
    a_19 = 3.05921
    
    T_c = 169.2 + 349.5*r_g - 74*r_g**2
    p_c = 756.8 - 131.07*r_g - 3.6*r_g**2
    temp = (9/5) *temp # convert K to R
    p_pr = p/p_c
    t_pr = temp/T_c
    t_pr_recip = 1/t_pr

    A = a_1*t_pr_recip*exp(a_2*(1-t_pr_recip)**2)*p_pr
    B = a_3*t_pr_recip + a_4*t_pr_recip**2+a_5*t_pr_recip**6*p_pr**6
    C = a_9 + a_8*t_pr_recip*p_pr + a_7*t_pr_recip**2*p_pr**2 + a_6*t_pr_recip**3*p_pr**3
    D = a_10*t_pr_recip*exp(a_11*(1-t_pr_recip)**2)
    E = a_12*t_pr_recip + a_13*t_pr_recip**2 + a_14*t_pr_recip**3
    F = a_15*t_pr_recip + a_16*t_pr_recip**2 + a_17*t_pr_recip**3
    G = a_18 + a_19*t_pr_recip
    y = (D*p_pr)/(((1+A**2)/C) - ((A**2*B)/(C**3)))

    result = ((D*p_pr*(1+y+y**2-y**3))/((D*p_pr+E*y**2-F*y**G)*(1-y)**3))
    return real(result)

def apparent_viscosity(vel, d2, d1, tau_y, mu_p, fluid_type = 'Bingham Plastic'):
    """
    Calculate the apparent viscosity based on the given parameters.
    
    Parameters:
        vel (float): The velocity of the fluid in ft/s.
        d2 (float): The diameter of the openhole in inch.
        d1 (float): The outer diameter of the pipe in inch.
        tau_y (float): The yield stress of fluid  in lbf/100ft^2.
        mu_p (float): The viscosity of the fluid in cp.
        fluid_type(non-dimensional) : There are two type of fluid. 'Bingham plastic' is one type of non-newtonian fluid and 'newton' is linear realtion shear stress between shear rate. 
    
    Returns:
        float: apparent viscosity in cp
    """
    
    if fluid_type.lower() == 'bingham plastic':
        mu_a = mu_p + 5*tau_y*(d2 - d1)/vel
    elif fluid_type.lower() =='newton':
        mu_a = mu_p
    else:
        assert False, 'The available fluid types are Newton, Bingham Pastic'
    return mu_a

def compute_gas_density(z, R, temp, kick_molar_mass, p_kick_pvt):
    """
    Calculate the gas density based on the given parameters.

    Parameters:
        z (non-dimensional): Z-factor
        R (float): The gas constant in J/mol-K.
        temp_well_before_kick_out (float): The temperature of the well before kick-out in K.
        kick_molar_mass (float): The molar mass of kick in g/mol.
        p_kick_pvt (float): The pressure at the middle of kick in psi.

    Returns:
        float: The computed gas density in ppg (pound per gallon).
    """
    return 0.05756*p_kick_pvt* kick_molar_mass/(z*R*temp)
   
   

