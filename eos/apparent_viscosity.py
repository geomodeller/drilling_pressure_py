
def apparent_viscosity(vel, openhole, pipe_OD, tau_y, mu_p, fluid_type = 'Bingham Plastic'):
    if fluid_type.lower() == 'bingham plastic':
        mu_a = mu_p + 5*tau_y*(openhole - pipe_OD)/vel
    elif fluid_type.lower() =='newton':
        mu_a = mu_p
    else:
        assert False, 'The available fluid types are Newton, Bingham Pastic'
    return mu_a