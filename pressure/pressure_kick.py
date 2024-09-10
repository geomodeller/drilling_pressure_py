
def pressure_kick_from_pvt(volume_kick, z, n, R, temp_well_before_kick_reaching):
    """
    Calculates the pressure kick based on the given volume_kick, z, n, R, and temp_well_before_kick_reaching values.

    Parameters:
    volume_kick (float): The volume of kick in bbl. 
    z (non-dimensional): The z factor.
    n (float): The number of Mole in mol.
    R (float): The R value in  Pa*m3/mol/K.
    temp_well_before_kick_reaching (float): The temperature of the well before the kick out in k.

    Returns:
    float: The calculated pressure of kick middle with pvt in psi.

    Note:
    0.000145 and 6.2933 are unit conversion factor (SI => BG)
    """
    return  0.000145 * 6.2933 *(z * n * R * temp_well_before_kick_reaching)/volume_kick


def pressure_kick_from_hy(p_kick_bottom, p_hy_by_kick):
    """
    Calculates the pressure kick based on the given values.

    Parameters:
    p_kick_bottom (float): The pressure of kick bottom in psi. 
    p_hy_by_kick (float): The hydraulic pressure of kick in psi.

    Returns:
    float: The calculated pressure of kick middle with hydraulic pressure method in psi.
    """
    return p_kick_bottom - p_hy_by_kick/2 