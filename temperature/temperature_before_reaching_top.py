def temperature_before_reaching_top(T, Formation_temperature_grad, kick_height_from_bh):
    """
    Calculates the temperature of the well before reaching the top based on the input parameters.

    Parameters:
    T (float): The initial temperature at the bottom of the well.
    Formation_temperature_grad (float): The temperature gradient of the formation.
    kick_height_from_bh (float): The height from the bottom of the well to the kick.

    Returns:
    float: The temperature of the well before reaching the top.
    """
    temp_well_before_kick_out = ((T + Formation_temperature_grad*(10000-kick_height_from_bh)/100) +459.67)*(5/9)
    return temp_well_before_kick_out
