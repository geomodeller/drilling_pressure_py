
def temperature_after_reaching_top(T, Formation_temperature_grad, cal_f_depth_between):
    """
    Calculate the temperature of the well after reaching the top during a kick out event.

    Parameters:
    T (float): Initial temperature of the well.
    Formation_temperature_grad (float): Formation temperature gradient.
    cal_f_depth_between (float): Depth between the kick depth and the formation top.

    Returns:
    float: The temperature of the well after reaching the top during a kick out event.
    """
    temp_well_to_during_kick_out = ((T + Formation_temperature_grad*(cal_f_depth_between)/100) +459.67)*(5/9)
    return temp_well_to_during_kick_out