
def compute_volume_of_kick_in_bottom(P_k_m_r, z, n, R, temp_well_before_kick_out):
    return 0.000145 * 6.2933 * (z * n * R * temp_well_before_kick_out )/(P_k_m_r)
    