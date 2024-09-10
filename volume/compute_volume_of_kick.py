
def compute_volume_of_kick(p_kick_pvt, z, n, R, temp_well_before_kick_reaching):
    """
    Calculate the volume of kick based on the given parameters.
    
    Parameters:
        p_kick_pvt (float): The pressure of kick middle with pvt in psi.
        z (Non-dimensional): The z factor.
        n (float): The number of Mole in mol.
        R (float): The R value in  Pa*m3/mol/K.
        temp_well_before_kick_out (float): The temperature when kick before reaching in K.
    
    Returns:
        float: 
    """
    return 0.000145 * 6.2933 * (z * n * R * temp_well_before_kick_reaching )/(p_kick_pvt)
    