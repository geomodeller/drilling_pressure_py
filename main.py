from temperature.temperature_before_reaching_top import temperature_before_reaching_top
from volume.inside_capacity import inside_capacity
from volume.find_depth_between import find_depth_between
from pressure.pressure_kick_bottom import pressure_kick_bottom
from pressure.pressure_kick import pressure_kick_from_hy, pressure_kick_from_pvt
from pressure.pressure_hy_by_kick import pressure_hy_by_kick
from eos.compute_gas_density import compute_gas_density

def main():
    bhp = 7280
    m_rho = 14
    k_molar_mass = 16.43 ## g*mol^(-1)
    
    depth = 10_000 ##in ft
    pipe_ID = 4.25 ## inch
    pipe_OD = 5 ## inch
    openhole = 9.5 ## inch
    
    volume = 30  ## bbl 30 bbl 들어왔다고 가정
    
    ## TODO: compute mass from PVT equaiton. Note that P_k_ini = bhp
    mass =  1_427_789.12 ## g, if density of kick = 2.5 ppg
    n = mass / k_molar_mass

    T = 77 ## F, 섭씨 25도

    ## TODO: z-factor should be described by a function of T and P
    z = 1
    R = 8.314
    mu_p = 16 # in cp 
    tau_y = 8 # in lbf/100ft^2
    q = 100   # in gpm, kill rate
    roughness = 0.000175 * 100 / 2.54 
    rel_roughness = roughness / pipe_ID
    Formation_temperature_grad = 2.0
    kick_height_from_bh = 0

    # step 1 - distribute temperature and determine flow regime
    temp_well_before_kick_out = temperature_before_reaching_top(T, Formation_temperature_grad, kick_height_from_bh)
    ID_c = inside_capacity(openhole, pipe_OD)
    f_depth_between = find_depth_between(ID_c, volume)
    kick_height_from_bh = 0

    P_k_b = pressure_kick_bottom(kick_height_from_bh, bhp, m_rho)
    p_k_z = pressure_kick_from_pvt(volume, z, n, R, temp_well_before_kick_out)
    k_rho = compute_gas_density(z, R, temp_well_before_kick_out, k_molar_mass, p_k_z)
    P_hy_bw = pressure_hy_by_kick(k_rho, f_depth_between)
    P_k_m_r = pressure_kick_from_hy(P_k_b, P_hy_bw) 
    vel = velocity(q, openhole, pipe_OD)
    mu_a = apparent_viscosity(vel, openhole, pipe_OD, tau_y, mu_p)
    Re = reynolds(m_rho, vel, openhole, pipe_OD, mu_a)

    if Re > 4000:
        f = friction_factor(Re, rel_roughness)
        dP_per_dL = pressure_gradient_turbulent(f, m_rho, vel, openhole, pipe_OD)
    elif Re < 2100:
        dP_per_dL = pressure_gradient_laminar(mu_p, tau_y, vel, openhole, pipe_OD)
    else:
        assert False, "Again, we cannot solve this task as 2,100 < Re < 4,000"

    v_k_x = volume
    cal_f_depth_between = cal_find_depth_between(ID_c, v_k_x)

    ## TODO: continue...

    pass


if __name__ =='__main__':
    main()