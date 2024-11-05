def annulus_capacity(openhole, pipe_OD):
    """
    Calculate the inside capacity based on the given parameters.
    
    Parameters:
        openhole (float): The diameter of openhole in inch.
        pipe_OD (float): The outer diameter of the pipe in inch.
        
    Returns:
        float: Inside capacity of fluid in bbl/ft.
    """
    return (openhole**2- pipe_OD**2)/ 1029.4 

def calculate_depth(ann_capacity, volume_kick):
    """
    Calculate the depth of fluid based on the given parameters.
    
    Parameters:
        ann_capacity (float): The annulus capacity in bbl/ft.
        volume_kick (float): The volume of kick in bbl.
        
    Returns:
        float: Depth of the kick in ft. 
    """
    return volume_kick / ann_capacity

def compute_volume_of_kick(p_kick_pvt, z, n, R, temp):
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
    return 0.000145 * 6.2933 * (z * n * R * temp )/(p_kick_pvt)