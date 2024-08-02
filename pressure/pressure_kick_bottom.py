
def pressure_kick_bottom(kick_height_from_bh, bhp, m_rho):
    
    """
    Calculate the pressure of kick bottom.
    
    Parameters:
    kick_height_from_bh (float): The depth when kick before reaching top in ft.  
    bhp (float): The pressure of bottomhole in psi.
    m_rho(float): The density of mud in ppg.

    Returns:
    float: The calculated hydraulic pressure in psi.
    """
       
    return bhp - 0.052 * kick_height_from_bh * m_rho