
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
      