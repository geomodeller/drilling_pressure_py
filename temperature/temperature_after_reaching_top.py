
def temperature_after_reaching_top(T_surface, Formation_temperature_grad, depth_of_kick):
    """
    Calculate the temperature of the well after reaching the top during a kick out event.

    Parameters:
    T (float): The initial temperature of the well in F.
    Formation_temperature_grad (float): The formation temperature gradient in F/100ft.
    depth_of_kick (float): The depth of kick in ft.

    Returns:
    float: The temperature of the well after reaching the top during a kick out event in K.
    """
    return ((T_surface + Formation_temperature_grad*(depth_of_kick)/100)-32)*(5/9)+273.15