
def pressure_hy_by_kick(k_rho, f_depth_between):

    """
    Calculate the hydraulic pressure due to a kick.
    
    Parameters:
    k_rho (float): The gas density in ppg.
    f_depth_between (float): The depth when kick afer go out surface in ft.
    
    Returns:
    float: The calculated hydraulic pressure in psi.
    """
    return 0.052 * k_rho * f_depth_between / 2

