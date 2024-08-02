
def temperature_after_reaching_top(T, Formation_temperature_grad, cal_f_depth_between):
    """
    Calculate the temperature of the well after reaching the top during a kick out event.

    Parameters:
    T (float): The initial temperature of the well in F.
    Formation_temperature_grad (float): The formation temperature gradient in F/100ft.
    cal_f_depth_between (float): The depth of kick in ft.

    Returns:
    float: The temperature of the well after reaching the top during a kick out event in K.
    """
    return ((T + Formation_temperature_grad*(cal_f_depth_between)/100) +459.67)*(5/9)