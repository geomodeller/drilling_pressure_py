def calculate_pressure_kick_bottom(kick_height_from_bh, bhp, mud_density, dP_per_dL):
    
    """
    Calculate the pressure of kick bottom.
    
    Parameters:
    kick_height_from_bh (float): The depth when kick before reaching top in ft.  
    bhp (float): The pressure of bottomhole in psi.
    mud_density(float): The density of mud in ppg.

    Returns:
    float: The calculated hydraulic pressure in psi.
    """
       
    return bhp - 0.052 * kick_height_from_bh * mud_density -dP_per_dL*(kick_height_from_bh)

def calculate_kick_Pseudo_reduced_pressure(p_kick_pvt, p_c):
    return p_kick_pvt/p_c

def choke_pressure(p_kick_top, mud_density, depth, dP_per_dL, kick_height_from_bh, depth_of_kick):
    
    """"
    Calculate the choke pressure based on the given parameters.

    Parameters:
        p_kick_top (float): The pressure of the kick top in psi. 
        mud_density (float): The density of mud in ppg.
        depth (float): The depth of well in ft.
        dP_per_dL (float): The frictional pressure gradient in psi/ft.
        kick_height_from_bh (float): The depth when kick before reaching top in ft.
        depth_of_kick (float): The depth when kick after go out surface in ft.

    Returns:
        float: The choke pressure when kick go out in psi.
    """    
    
    return p_kick_top - 0.052 * mud_density * (depth-kick_height_from_bh-depth_of_kick) - dP_per_dL * (depth-kick_height_from_bh-depth_of_kick)

def pressure_gradient_laminar(mu_p, tau_y, vel, openhole, pipe_OD):
  
   """"
    Calculate the pressure gradient when flow is laminar based on the given parameters.

    Parameters:
        mu_p (float): The viscosity of the fluid in cp
        tau_y (float): The yield stress of fluid  in lbf/100ft^2.
        vel (float): The velocity of the fluid in ft/s.
        openhole (float): The outer diameter of the pipe in inch.
        pipe_OD (float): The inner diameter of the pipe in inch.

    Returns:
        float: The pressure gradient when flow is laminar
    """
   return mu_p*vel/(1000* (openhole- pipe_OD)**2) + tau_y/(200 *(openhole - pipe_OD)) 

def pressure_gradient_turbulent(f, m_rho, vel, openhole, pipe_OD):
    
    """"
    Calculate the pressure gradient when flow is turbulent based on the given parameters.

    Parameters:
        f (Non-dimensional): The friction factor.
        m_rho (float): The density of mud in ppg.
        vel (float): The velocity of the fluid in ft/s.
        openhole (float): The outer diameter of the pipe in inch.
        pipe_OD (float): The inner diameter of the pipe in inch.

    Returns:
        float: The pressure gradient when flow is turbulent
    """
    return f*m_rho*vel**2/21.1/(openhole - pipe_OD)

def pressure_hy_by_kick(kick_density, depth_of_kick):

    """
    Calculate the hydraulic pressure due to a kick.
    
    Parameters:
    kick_density (float): The gas density in ppg.
    depth_of_kick (float): The depth of kick possess in ft.
    
    Returns:
    float: The calculated hydraulic pressure in psi.
    """
    return 0.052 * kick_density * depth_of_kick


def pressure_kick_top(p_kick_from_hy, p_hy_of_kick):
    
    """
    Calculate the pressure of kick top.
    
    Parameters:
    p_kick_from_hy (float): The pressure of kick middle with hydraulic pressure in psi.  
    p_hy_of_kick (float): The hydraulic pressure of kick in psi. 

    Returns:
    float: The pressure of kick top in psi.
    """
    
    return p_kick_from_hy - p_hy_of_kick


def pressure_kick_from_pvt(volume_kick, z, n, R, temp):
    """
    Calculates the pressure kick based on the given volume_kick, z, n, R, and temp_well_before_kick_reaching values.

    Parameters:
    volume_kick (float): The volume of kick in bbl. 
    z (non-dimensional): The z factor.
    n (float): The number of Mole in mol.
    R (float): The R value in  Pa*m3/mol/K.
    temp_well_before_kick_reaching (float): The temperature of the well before the kick out in k.

    Returns:
    float: The calculated pressure of kick middle with pvt in psi.

    Note:
    0.000145 and 6.2933 are unit conversion factor (SI => BG)
    """
    return  0.000145 * 6.2933 *(z * n * R * temp)/volume_kick


def pressure_kick_from_hy(p_kick_bottom, p_hy_by_kick):
    """
    Calculates the pressure kick based on the given values.

    Parameters:
    p_kick_bottom (float): The pressure of kick bottom in psi. 
    p_hy_by_kick (float): The hydraulic pressure of kick in psi.

    Returns:
    float: The calculated pressure of kick middle with hydraulic pressure method in psi.
    """
    return p_kick_bottom - p_hy_by_kick/2 