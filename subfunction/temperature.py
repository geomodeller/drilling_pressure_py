def calculate_kick_Pseudo_reduced_temperature_before_kick_reaching(temp_well_before_kick_reaching, T_c):
    return (9/5)*(temp_well_before_kick_reaching)/T_c
    
def calculate_kick_Pseudo_reduced_temperature_during_kick_out(temp_well_to_during_kick_out, T_c):
    return (9/5)*(temp_well_to_during_kick_out)/T_c


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

def temperature_before_reaching_top(T_surface, Formation_temperature_grad, kick_height_from_bh):
    """
    Calculates the temperature of the well before reaching the top based on the input parameters.

    Parameters:
    T_surface (float): The initial temperature at the surface of the well in F.
    Formation_temperature_grad (float): The temperature gradient of the formation in F/100ft.
    kick_height_from_bh (float): The height from the bottom of the well to the kick in ft.

    Returns:
    float: The temperature of the well before reaching the top in K.
    """
    return (((T_surface + Formation_temperature_grad*(10000-kick_height_from_bh)/100)-32)*(5/9)+273.15)
