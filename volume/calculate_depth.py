
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