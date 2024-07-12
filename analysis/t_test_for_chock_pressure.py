
from scipy.stats import ttest_rel
def t_test_for_chock_pressure(normalized_data, max_choke_pressures):
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