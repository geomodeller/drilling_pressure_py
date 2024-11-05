from math import log, nan

def friction_factor(Re, rel_roughness):
    
    """
    Calculates the friction factor for a fluid flow. 

    Args:
        Re (float): The Reynolds number, which is a dimensionless quantity that characterizes the flow.
        rel_roughness (float): The relative roughness of the pipe.

    Returns:
        float: The friction factor, which is a dimensionless quantity that represents the resistance to flow in a fluid.

    Note:
        The friction factor is calculated based on the Reynolds number and relative roughness of the pipe. If the Reynolds number is greater than 4000, the turbulent flow equation is used. Otherwise, the laminar flow equation is used.
        This is fanning factor, not Moody factor
    """
    if Re>4000:
        # when it's turbulent
        A_0 = -0.79638*log(rel_roughness/8.208 + 7.3357/Re)
        A_1 = Re*rel_roughness + 9.3120665*A_0
        f = ((8.128943 + A_1)/(8.128943*A_0 - 0.86859209*A_1*log(A_1/3.7099535/Re)))**2
    elif Re < 2100:
        # When it's laminar 
        f = 64/Re
    else:
        f = nan
    return f/4 


def reynolds(mud_density, vel, mu_a, d1, d2, openhole, is_annulus = True):
    """
    Calculate the Reynolds number based on the given parameters.

    Parameters:
        mud_density (float): The mass density of the fluid in ppg
        vel (float): The velocity of the fluid in ft/s
        mu_a (float): The dynamic viscosity of the fluid in cp
        d1 (float): The inner diameter of the pipe in inch
        d2 (float, optional): The outer diameter of the pipe in inch. Defaults to None.
        openhole (float): The diameter of openhole in inch.
        is_annulus (bool, optional): Flag indicating if the pipe is an annulus. Defaults to True.

    Returns:
        float: The Reynolds number.


    Notes:
        - The function calculates the Reynolds number based on the given parameters.
        - The formula used to calculate the Reynolds number depends on the value of `is_annulus`.
        - If `is_annulus` is True, the function calculates the Reynolds number for an annular pipe.
        - If `is_annulus` is False, the function calculates the Reynolds number for a cylindrical pipe.

    Examples:
        >>> reynolds(1000, 10, 0.01, 0.1, 0.2, is_annulus=True)
        _____
        >>> reynolds(1000, 10, 0.01, 0.2, 0.1, is_annulus=True)
        _____
        >>> reynolds(1000, 10, 0.01, 0.1, is_annulus=False)
        _____
    """
    if is_annulus:
        return 928* 0.816 * mud_density*vel*(openhole - d2)/mu_a
    else:
        return 928 * mud_density*vel*(d1)/mu_a
       
def velocity_pipe_inside(kill_rate, pipe_ID):
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
     return kill_rate / 2.448 / (pipe_ID**2)
