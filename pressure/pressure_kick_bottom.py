
def pressure_kick_bottom(kick_height_from_bh, bhp, m_rho):
    P_k_b = bhp - 0.052 * kick_height_from_bh * m_rho 
    return P_k_b