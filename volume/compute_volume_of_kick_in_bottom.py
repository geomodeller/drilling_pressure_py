
def compute_volume_of_kick_in_bottom(P_k_m_r, z, n, R, temp_well_before_kick_out):
    """
    Calculate the apparent viscosity based on the given parameters.
    
    Parameters:
        P_k_m_r (float): The pressure of kick middle with pvt in psi.
        z (Non-dimensional): The z factor.
        n (float): The number of Mole in mol.
        R (float): The R value in  Pa*m3/mol/K.
        temp_well_before_kick_out (float): The temperature when kick before reaching in K.
    
    Returns:
        float: 
    """
    return 0.000145 * 6.2933 * (z * n * R * temp_well_before_kick_out )/(P_k_m_r)
    