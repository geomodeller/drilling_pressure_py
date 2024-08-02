
def time_conversion_before_reaching_top(vel, kick_height_from_bh):
     """
    Calculate time conversion depth to time when kick before reaching top. 

    Parameters:
        vel(float): The velocity of fluid in ft/s.
        kick_height_from_bh (float): The depth of kick height from bottomhole in ft.
        
    Returns: 
        float: Time when kick before reaching top in s.   
    """
     return kick_height_from_bh / vel

def time_conversion_ater_reaching_top(vel, t, cal_f_depth_between):
     """
    Calculate time conversion depth to time when kick after go out surface.

    Parameters:
        vel(float): The velocity of fluid in ft/s.
        t(float): The time when kick before reaching top in s.
        cal_f_depth_between (float): The depth of kick depth after go out surface in ft. 
        
    Returns: 
        float: Time when kick after go out surface in s.  
    """
     return t + cal_f_depth_between/vel
