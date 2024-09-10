import pandas as pd
import math 

from pressure.calculate_pressure_kick_bottom import calculate_pressure_kick_bottom
from pressure.pressure_kick import pressure_kick_from_hy, pressure_kick_from_pvt
from pressure.pressure_gradient import pressure_gradient_laminar
from pressure.pressure_gradient import pressure_gradient_turbulent
from pressure.pressure_hy_by_kick import pressure_hy_by_kick
from pressure.pressure_kick_top import pressure_kick_top
from pressure.chock_pressure import choke_pressure
from pressure.calculate_Pseudo_reduced_pressure import calculate_kick_Pseudo_reduced_pressure
from volume.annulus_capacity import annulus_capacity
from volume.calculate_depth import calculate_depth
from volume.compute_volume_of_kick import compute_volume_of_kick
from temperature.temperature_after_reaching_top import temperature_after_reaching_top
from temperature.temperature_before_reaching_top import temperature_before_reaching_top
from temperature.calculate_Pseudo_reduced_temperature import calculate_kick_Pseudo_reduced_temperature_before_kick_reaching
from eos.calculate_z_factor import calculate_z_factor
from eos.compute_gas_density import compute_gas_density
from eos.apparent_viscosity import apparent_viscosity
from flow.reynolds import reynolds
from flow.velocity import velocity
from flow.friction_factor import friction_factor
from miscellaneous.depth_to_time import time_conversion_before_reaching_top
from miscellaneous.depth_to_time import time_conversion_ater_reaching_top

def compute_kick_behavior(bhp:float, 
                          kick_molar_mass:float,
                          mud_density:float,
                          depth:float = 10000.,
                          pipe_ID: float = 4.25,
                          pipe_OD: float = 5.0,
                          roughness: float = 0.00689,
                          openhole: float = 9.5,
                          r_g: float = 0.554,
                          volume_kick: float = 30.,
                          T_surface: float = 77.,
                          mu_p: float = 16.,
                          tau_y: float = 8,
                          q: float = 150.,
                          formation_temperature_grad: float = 2.0,
                          fluid_type: str = 'Bingham Plastic',
                          )->pd.DataFrame:
    """compute_kick_behavior

    Parameters
    ----------
    bhp : float
        bottom hole pressure, psi
    kick_molar_mass : float
        kick molar mass in g/mol
    mud_density : float
        density of mass in ppg
    depth : float, optional
        total depth of well in ft, by default 10000.
    pipe_ID : float, optional
        internal pipe diameter in inches, by default 4.25
    pipe_OD : float, optional
        external pipe diameter in inches, by default 5.0
    roughness : float, optional
         
    openhole : float, optional
        openhole diameter in inches, by default 9.5
    r_g: float, optional
        specific gravity, by 0.54
    volume_kick : float, optional
        kick volume in bbl, by default 30.
    T_surface : float, optional
        surface temperature in Farenheit, by default 77
    mu_p : float, optional
    
    tau_y : float, optional
    
    q : float, optional
        
    formation_temperature_grad : float, optional
        
    fluid_type : str, optianla
        
    Returns
    -------
    pd.DataFrame
        data frame that contains depth, kick volume, temperature
        chock pressure, time 
    """
           
    ## Basic numerical settings for precision control:
    numerical_threshold = 1.0
    numerical_kick_volume_increment = 0.001

    # ideal gas constant
    z = 1.0 # intial assumption
    R = 8.314 # J/(mol*k)
    kick_height_from_bh = 0
    temp_well_before_kick_reaching = temperature_before_reaching_top(T_surface, formation_temperature_grad, kick_height_from_bh)
    mass = (1/(0.000145*6.29326))*(bhp*volume_kick*kick_molar_mass)/(z*R*(temp_well_before_kick_reaching))
    n = mass / kick_molar_mass
    rel_roughness = roughness / pipe_ID
    T_c = 169.2 + 349.5*r_g - 74*r_g**2
    p_c = 756.8 - 131.07*r_g - 3.6*r_g**2

    # step 1 - distribute temperature and determine flow regime
    ann_capacity = annulus_capacity(openhole, pipe_OD)
    depth_of_kick = calculate_depth(ann_capacity, volume_kick)
    p_kick_pvt = pressure_kick_from_pvt(volume_kick, z, n, R, temp_well_before_kick_reaching)
    p_pr = calculate_kick_Pseudo_reduced_pressure(p_kick_pvt, p_c)
    t_pr = calculate_kick_Pseudo_reduced_temperature_before_kick_reaching(temp_well_before_kick_reaching, T_c)
    z = calculate_z_factor(p_kick_pvt,temp_well_before_kick_reaching)
    vel = velocity(q, pipe_ID, pipe_OD, openhole)
    mu_a = apparent_viscosity(vel, pipe_OD, pipe_ID, tau_y, mu_p, fluid_type = fluid_type)
    Re = reynolds(mud_density, vel, mu_a, pipe_ID, pipe_OD, openhole, is_annulus = True)
    
    if Re > 4000:
        f = friction_factor(Re, rel_roughness)
        dP_per_dL = pressure_gradient_turbulent(f, mud_density, vel, openhole, pipe_OD)
    elif Re < 2100:
        dP_per_dL = pressure_gradient_laminar(mu_p, tau_y, vel, openhole, pipe_OD)
    else:
        assert False, "Again, we cannot solve this task as 2,100 < Re < 4,000"
    
    ## step 2 - until top of kick before reaching surface
    depth_list = []
    pressure_kick_top_list = []
    pressure_ch_list = []
    volume_kick_list = []
    temp_well_before_kick_reaching_list = []
    time_kick_before_reaching_top_list = []
    
    step = 1
    while  depth > kick_height_from_bh and depth-kick_height_from_bh > depth_of_kick:
        volume_from_bh_to_surface = 0

        while abs(volume_from_bh_to_surface-volume_kick) > numerical_threshold:
            volume_kick_at_x = volume_kick            
            
            temp_well_before_kick_reaching = temperature_before_reaching_top(T_surface, formation_temperature_grad, kick_height_from_bh)
            p_kick_bottom = calculate_pressure_kick_bottom(kick_height_from_bh, bhp, mud_density)
            p_kick_pvt = pressure_kick_from_pvt(volume_kick, z, n, R, temp_well_before_kick_reaching)
            z = calculate_z_factor(p_kick_pvt,temp_well_before_kick_reaching)
            kick_density = compute_gas_density(z, R, temp_well_before_kick_reaching, kick_molar_mass, p_kick_pvt)
            ann_capacity = annulus_capacity(openhole, pipe_OD)
            depth_of_kick = calculate_depth(ann_capacity, volume_kick)
            p_hy_of_kick = pressure_hy_by_kick(kick_density, depth_of_kick)
            p_kick_from_hy = pressure_kick_from_hy(p_kick_bottom, p_hy_of_kick)
            volume_from_bh_to_surface = compute_volume_of_kick(p_kick_pvt, z, n, R, temp_well_before_kick_reaching)
            time_kick_before_reaching_top = time_conversion_before_reaching_top(vel, kick_height_from_bh)
            volume_kick += numerical_kick_volume_increment
        
        temp_well_before_kick_reaching = temperature_before_reaching_top(T_surface, formation_temperature_grad, kick_height_from_bh)
        p_hy_of_kick = pressure_hy_by_kick(kick_density, depth_of_kick)
        p_kick_from_hy = pressure_kick_from_hy(p_kick_bottom, p_hy_of_kick) 
        p_kick_top = pressure_kick_top(p_kick_from_hy, p_hy_of_kick)
        pressure_ch = choke_pressure(p_kick_top, mud_density, depth, dP_per_dL, kick_height_from_bh, depth_of_kick)
        time_kick_before_reaching_top = time_conversion_before_reaching_top(vel, kick_height_from_bh)

        depth_list.append(kick_height_from_bh)
        pressure_kick_top_list.append(p_kick_top)
        pressure_ch_list.append(pressure_ch)
        volume_kick_list.append(volume_kick)
        time_kick_before_reaching_top_list.append(time_kick_before_reaching_top)
        temp_well_before_kick_reaching_list.append(temp_well_before_kick_reaching)
        kick_height_from_bh += step
    

        
    df_before_exit = pd.DataFrame({'kick_height_from_bh': depth_list, 
                                        'choke_pressure': pressure_ch_list, 
                                        'methane_volume_when_go_surface_before': volume_kick_list,
                                        'time': time_kick_before_reaching_top_list,
                                        'temperature_of_well': temp_well_before_kick_reaching_list})
    df_before_exit['depth'] = depth - df_before_exit['kick_height_from_bh']
    
    ## step 3 - during kick go out  

    volume_kick_during_go_out_list = []
    depth_of_kick_list = []
    temp_well_to_during_kick_out_list = []
    time_after_reacing_top_list = []
    pressure_ch_during_go_out_list = []
    
    while volume_kick_at_x > 0:
        time_after_reacing_top = time_conversion_ater_reaching_top(vel, time_kick_before_reaching_top, depth_of_kick)
        depth_of_kick = calculate_depth(ann_capacity, volume_kick)
        p_hy_of_kick = pressure_hy_by_kick(kick_density, depth_of_kick)
        p_kick_from_hy = pressure_kick_from_hy(p_kick_bottom, p_hy_of_kick) 
        p_kick_top = pressure_kick_top(p_kick_from_hy, p_hy_of_kick)
        temp_well_to_during_kick_out = temperature_after_reaching_top(T_surface, formation_temperature_grad, depth_of_kick)
        pressure_ch = choke_pressure(p_kick_top, mud_density, depth, dP_per_dL, kick_height_from_bh, depth_of_kick)
        
        volume_kick_during_go_out_list.append(volume_kick_at_x)
        depth_of_kick_list.append(depth_of_kick)
        pressure_ch_during_go_out_list.append(pressure_ch)
        time_after_reacing_top_list.append(time_after_reacing_top)
        temp_well_to_during_kick_out_list.append(temp_well_to_during_kick_out)

        volume_kick_at_x -= numerical_kick_volume_increment
     

    ## step 4 - data arrange 
            
    time_after_reacing_top_list_reversed = list(reversed(time_after_reacing_top_list))

    df_after_exit = pd.DataFrame({'methane_volume_when_kick_go_surface': volume_kick_during_go_out_list,
                                        'depth_of_kick': depth_of_kick_list, 
                                        'choke_pressure': pressure_ch_during_go_out_list,
                                        'time2': time_after_reacing_top_list_reversed,
                                        'temperatrue_of_well': temp_well_to_during_kick_out_list})


    df_1 = df_after_exit[['time2',
                          'methane_volume_when_kick_go_surface',
                          'choke_pressure']]
    df_0 = df_before_exit[['time',
                           'methane_volume_when_go_surface_before', 
                           'choke_pressure']]
    df_0 = df_0.rename(columns={"time":"time", 
                                "methane_volume_when_go_surface_before":"kick_volume", 
                                "choke_pressure":"choke_pressure" })
    df_1 = df_1.rename(columns={"time2":"time", 
                                "methane_volume_when_kick_go_surface":"kick_volume", 
                                "choke_pressure":"choke_pressure" })
    df = pd.concat([df_0,df_1], axis = 0).reset_index()
            

    return df