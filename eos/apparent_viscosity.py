
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