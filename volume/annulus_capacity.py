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