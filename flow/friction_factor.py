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