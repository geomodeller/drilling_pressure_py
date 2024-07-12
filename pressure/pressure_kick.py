
def pressure_kick_from_pvt(volume, z, n, R, temp_well_before_kick_out):
    """
    Calculates the pressure kick based on the given volume, z, n, R, and temp_well_before_kick_out values.

    Parameters:
    volume (float): The volume value [bbls]. 
    z (float): The z value.
    n (float): The n value. The number of Mole
    R (float): The R value. [Pa*m3/mol/K]
    temp_well_before_kick_out (float): The temperature of the well before the kick out [Kevin].

    Returns:
    float: The calculated pressure kick [psi].

    Note:
    0.000145 and 6.2933 are unit conversion factor (SI => BG)
    """
    return  0.000145 * 6.2933 *(z * n * R * temp_well_before_kick_out)/volume


def pressure_kick_from_hy(P_k_b, P_hy_bw):
    P_k_m_r = P_k_b - P_hy_bw
    return P_k_m_r 