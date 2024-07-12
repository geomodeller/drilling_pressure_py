
    

def choke_pressure(p_k_t, m_rho, depth, dP_per_dL, kick_height_from_bh, cal_f_depth_between):
    ch_pressure2 = p_k_t - 0.052 * m_rho * (depth-kick_height_from_bh-cal_f_depth_between) - dP_per_dL * (10000-depth)
    return ch_pressure2