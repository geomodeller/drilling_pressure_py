
    

def choke_pressure(p_k_t, m_rho, depth, dP_per_dL, kick_height_from_bh, cal_f_depth_between):
    
    """"
    Calculate the choke pressure based on the given parameters.

    Parameters:
        p_k_t (float): The pressure of the kick top in psi. 
        m_rho (float): The density of mud in ppg.
        depth (float): The depth of well in ft.
        dP_per_dL (float): The frictional pressure gradient in psi/ft.
        kick_height_from_bh (float): The depth when kick before reaching top in ft.
        cal_f_depth_between (float): The depth when kick after go out surface in ft.

    Returns:
        float: The choke pressure when kick go out in psi.
    """    
    
    return p_k_t - 0.052 * m_rho * (depth-kick_height_from_bh-cal_f_depth_between) - dP_per_dL * (10000-depth)