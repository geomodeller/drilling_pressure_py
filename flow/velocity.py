def velocity(q, openhole, pipe_OD):
     """
    Calculate average velocity based on the given parameters.

    Parameters:
        q (float): The flow rate of fluid in gpm.
        d1 (float): The inner diameter of the pipe in inch.
        d2 (float): The outer diameter of the pipe in inch.
        
    Returns: 
        float: velocity of the fluid in ft/s. 
    """
     return q / 2.448 / (openhole**2 - pipe_OD**2)
