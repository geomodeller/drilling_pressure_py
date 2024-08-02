
def pressure_kick_from_pvt(volume, z, n, R, temp_well_before_kick_out):
    """
    Calculates the pressure kick based on the given volume, z, n, R, and temp_well_before_kick_out values.

    Parameters:
    volume (float): The volume value in bbl. 
    z (non-dimensional): The z factor.
    n (float): The number of Mole in mol.
    R (float): The R value in  Pa*m3/mol/K.
    temp_well_before_kick_out (float): The temperature of the well before the kick out in k.

    Returns:
    float: The calculated pressure of kick middle with pvt in psi.

    Note:
    0.000145 and 6.2933 are unit conversion factor (SI => BG)
    """
    return  0.000145 * 6.2933 *(z * n * R * temp_well_before_kick_out)/volume


def pressure_kick_from_hy(P_k_b, P_hy_bw):
    """
    Calculates the pressure kick based on the given volume, z, n, R, and temp_well_before_kick_out values.

    Parameters:
    P_k_b (float): The pressure of kick bottom in psi. 
    P_hy_bw (float): The hydraulic pressure of kick in psi.

    Returns:
    float: The calculated pressure of kick middle with hydraulic pressure method in psi.
    """
    return P_k_b - P_hy_bw 