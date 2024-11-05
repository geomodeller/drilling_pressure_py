
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