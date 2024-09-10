
    

def choke_pressure(p_kick_top, mud_density, depth, dP_per_dL, kick_height_from_bh, depth_of_kick):
    
    """"
    Calculate the choke pressure based on the given parameters.

    Parameters:
        p_kick_top (float): The pressure of the kick top in psi. 
        mud_density (float): The density of mud in ppg.
        depth (float): The depth of well in ft.
        dP_per_dL (float): The frictional pressure gradient in psi/ft.
        kick_height_from_bh (float): The depth when kick before reaching top in ft.
        cal_f_depth_between (float): The depth when kick after go out surface in ft.

    Returns:
        float: The choke pressure when kick go out in psi.
    """    
    
    return p_kick_top - 0.052 * mud_density * (depth-kick_height_from_bh-depth_of_kick) - dP_per_dL * (10000-depth)