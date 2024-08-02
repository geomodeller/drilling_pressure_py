def temperature_before_reaching_top(T, Formation_temperature_grad, kick_height_from_bh):
    """
    Calculates the temperature of the well before reaching the top based on the input parameters.

    Parameters:
    T (float): The initial temperature at the bottom of the well in F.
    Formation_temperature_grad (float): The temperature gradient of the formation in F/100ft.
    kick_height_from_bh (float): The height from the bottom of the well to the kick in ft.

    Returns:
    float: The temperature of the well before reaching the top in K.
    """
    return ((T + Formation_temperature_grad*(10000-kick_height_from_bh)/100) +459.67)*(5/9)
