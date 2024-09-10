
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

