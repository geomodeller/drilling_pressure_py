
def pressure_hy_by_kick(k_rho: float, f_depth_between: float) -> float:
    """
    Calculate the hydraulic pressure due to a kick.
    
    Parameters:
    k_rho (float): The gas density in ppg.
    f_depth_between (float): The depth between two positions in ft.
    
    Returns:
    float: The calculated hydraulic pressure in psi.
    """
    return 0.052 * k_rho * f_depth_between / 2

