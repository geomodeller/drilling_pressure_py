import numpy as np
from math import log, nan
from sklearn.preprocessing import StandardScaler
from scipy.stats import ttest_rel
  
def inside_capacity(openhole, pipe_OD):
    ID_c = (openhole**2- pipe_OD**2)/ 1029.4 
    return ID_c

def find_depth_between(ID_c, volume):
    f_depth_between = volume / ID_c
    return f_depth_between

def pressure_kick_bottom(kick_height_from_bh, bhp, m_rho):
    P_k_b = bhp - 0.052 * kick_height_from_bh * m_rho 
    return P_k_b

def pressure_kick_z(volume, z, n, R, temp_well_before_kick_out):
    p_k_z = 0.000145 * 6.2933 *(z * n * R * temp_well_before_kick_out)/volume
    return p_k_z

def compute_gas_density(z, R, temp_well_before_kick_out, molar_mass_methane, p_k_z):
    return 0.05756*p_k_z* molar_mass_methane/(z*R*temp_well_before_kick_out)
   
def P_hy_between(k_rho, f_depth_between):
    P_hy_bw = 0.052 * k_rho * f_depth_between / 2
    return P_hy_bw
    
def P_kick_middle_r(P_k_b, P_hy_bw):
    P_k_m_r = P_k_b - P_hy_bw
    return P_k_m_r 

def velocity(q, openhole, pipe_OD):
    vel = q / 2.448 / (openhole**2 - pipe_OD**2)
    return vel

def apparent_viscosity(vel, openhole, pipe_OD, tau_y, mu_p):
    mu_a = mu_p + 5*tau_y*(openhole - pipe_OD)/vel
    return mu_a

def reynolds(m_rho, vel, openhole, pipe_OD, mu_a):
    Re = 928* 0.816 * m_rho*vel*(openhole - pipe_OD)/mu_a
    return Re

def friction_factor(Re, rel_roughness):
    if Re>4000:
        # when it's turbulent
        A_0 = -0.79638*log(rel_roughness/8.208 + 7.3357/Re)
        A_1 = Re*rel_roughness + 9.3120665*A_0
        f = ((8.128943 + A_1)/(8.128943*A_0 - 0.86859209*A_1*log(A_1/3.7099535/Re)))**2
    elif Re < 2100:
        # When it's laminar 
        f = 64/Re
    else:
        f = nan
    return f/4 

def pressure_gradient_laminar(mu_p, tau_y, vel, openhole, pipe_OD):
    return mu_p*vel/(1000* (openhole- pipe_OD)**2) + tau_y/(200 *(openhole - pipe_OD)) 

def pressure_gradient_turbulent(f, m_rho, vel, openhole, pipe_OD):
    return f*m_rho*vel**2/21.1/(openhole - pipe_OD)
    
def volume_kick_z(P_k_m_r, z, n, R, temp_well_before_kick_out):
    return 0.000145 * 6.2933 * (z * n * R * temp_well_before_kick_out )/(P_k_m_r)
    
def cal_find_depth_between(ID_c, v_k_x):
    cal_f_depth_between = v_k_x / ID_c 
    return cal_f_depth_between

def cal_P_hy_between(k_rho, cal_f_depth_between):
    cal_P_hy_bw = 0.052 * k_rho * cal_f_depth_between/2 
    return cal_P_hy_bw
    
def cal_P_kick_middle_r(P_k_b, cal_P_hy_bw):
    cal_P_k_m_r = P_k_b - (cal_P_hy_bw)
    return cal_P_k_m_r
    
def pressure_kick_top(cal_P_k_m_r, cal_P_hy_bw):
    p_k_t = cal_P_k_m_r - cal_P_hy_bw
    return p_k_t  

def choke_pressure2(p_k_t, m_rho, depth, dP_per_dL, kick_height_from_bh, cal_f_depth_between):
    ch_pressure2 = p_k_t - 0.052 * m_rho * (depth-kick_height_from_bh-cal_f_depth_between) - dP_per_dL * (10000-depth)
    return ch_pressure2
    
def choke_pressure3(p_k_t, m_rho, depth, dP_per_dL, kick_height_from_bh, cal_f_depth_between):
    ch_pressure3 = p_k_t - 0.052 * m_rho*(depth-kick_height_from_bh-cal_f_depth_between) - dP_per_dL * (10000-depth)
    return ch_pressure3

def time(vel, kick_height_from_bh):
    t = kick_height_from_bh / vel
    return t

def time2(t, vel, cal_f_depth_between):
    t_2 = t + cal_f_depth_between/vel
    return t_2

def temperature_well_before_kick_out(T, Formation_temperature_grad, kick_height_from_bh):
    temp_well_before_kick_out = ((T + Formation_temperature_grad*(10000-kick_height_from_bh)/100) +459.67)*(5/9)
    return temp_well_before_kick_out

def temperature_well_to_during_kick_out(T, Formation_temperature_grad, cal_f_depth_between):
    temp_well_to_during_kick_out = ((T + Formation_temperature_grad*(cal_f_depth_between)/100) +459.67)*(5/9)
    return temp_well_to_during_kick_out
    
    
def perform_t_tests_kick_volume(normalized_data, max_kick_volumes):
    results = []
    for data, label in zip(normalized_data, ['bhp', 'm_rho', 'molar_mass']):
        t_stat, p_value = ttest_rel(data, max_kick_volumes)
        
        result_max_kick_volume = {
            'Variable_kick_volume': label,
            'T-statistic_kick_volume': t_stat,
            'P-value about max kick volume': p_value,
            'Significance': 'Significant' if p_value < 0.05 else 'Not significant'
        }
        results.append(result_max_kick_volume)

    results.sort(key=lambda x: abs(x['T-statistic_kick_volume']), reverse=True)
    
    most_influential_variable_kick_volume = results[0]['Variable_kick_volume'] 
    print("Most influential variable about max kick volume:", most_influential_variable_kick_volume)
    return results

    
def perform_t_tests_choke_pressure(normalized_data, max_choke_pressures):
    results = []
    for data, label in zip(normalized_data, ['bhp', 'm_rho', 'molar_mass']):
        t_stat, p_value = ttest_rel(data, max_choke_pressures)
        
        result_max_choke_pressure = {
            'Variable_choke_pressure': label,
            'T-statistic_choke_pressure': t_stat,
            'P-value about max choke pressure': p_value,
            'Significance': 'Significant' if p_value < 0.05 else 'Not significant'
        }
        results.append(result_max_choke_pressure)

    results.sort(key=lambda x: abs(x['T-statistic_choke_pressure']), reverse=True)
    
    most_influential_variable_choke_pressure = results[0]['Variable_choke_pressure']
    print("Most influential variable about max choke pressure:", most_influential_variable_choke_pressure)
    return results 
   
def normalize_data(*args):
    scaler = StandardScaler()
    normalized_data = []
    for data in args:
        data_np = np.array(data) 
        normalized_data.append(scaler.fit_transform(data_np.reshape(-1, 1)).flatten())
    return normalized_data
    
def solubility(P, T, f_300F, f_200F, f_100F):
    sol_300F = f_300F(P)
    sol_200F = f_200F(P)
    sol_100F = f_100F(P)
    if (T < 100) or (T >300):
        print('not available temperature!') 
        return np.nan
    elif (100<=T) and (T<200):
        slope = (sol_200F-sol_100F)/100
        sol = sol_100F + slope*(T-100)
        return sol
    elif (200<=T) and (T<=300):
        slope = (sol_300F-sol_200F)/100
        sol = sol_200F + slope*(T-200)
        return sol

