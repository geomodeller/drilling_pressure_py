def velocity_annulus(kill_rate, pipe_OD, openhole):
     """
    Calculate average velocity based on the given parameters.

    Parameters:
        kill_rate (float): The flow rate of fluid in gpm.
        d1 (float): The inner diameter of the pipe in inch.
        d2 (float): The outer diameter of the pipe in inch.
        openhole (float): The diameter of the openhole in inch.
       
        
    Returns: 
        float: velocity of the fluid in ft/s. 
    """
     return kill_rate / 2.448 / (openhole**2- pipe_OD**2)
