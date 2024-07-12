


def pressure_gradient_laminar(mu_p, tau_y, vel, openhole, pipe_OD):
    return mu_p*vel/(1000* (openhole- pipe_OD)**2) + tau_y/(200 *(openhole - pipe_OD)) 

def pressure_gradient_turbulent(f, m_rho, vel, openhole, pipe_OD):
    return f*m_rho*vel**2/21.1/(openhole - pipe_OD)
