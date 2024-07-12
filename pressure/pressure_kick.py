
def pressure_kick(volume, z, n, R, temp_well_before_kick_out):
    p_k_z = 0.000145 * 6.2933 *(z * n * R * temp_well_before_kick_out)/volume
    return p_k_z