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
