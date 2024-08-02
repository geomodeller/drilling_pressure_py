
def pressure_kick_top(cal_P_k_m_r, cal_P_hy_bw):
    
    """
    Calculate the pressure of kick top.
    
    Parameters:
    cal_P_k_m_r (float): The pressure of kick middle with pvt in psi.  
    cal_P_hy_bw (float): The hydraulic pressure of kick in psi. 

    Returns:
    float: The pressure of kick top in psi.
    """
    
    return cal_P_k_m_r - cal_P_hy_bw
      