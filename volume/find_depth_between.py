
def find_depth_between(ID_c, volume):
    """
    Calculate the depth of fluid based on the given parameters.
    
    Parameters:
        ID_c (float): The inside capacity in bbl/ft.
        volume (float): The volume of kick in bbl.
        
    Returns:
        float: Depth of the kick in ft. 
    """
    return volume / ID_c