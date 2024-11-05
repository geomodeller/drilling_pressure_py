from scipy.stats import ttest_rel

def t_test_for_kick_volume(normalized_data, max_kick_volumes):
    results = []
    for data, label in zip(normalized_data, ['bhp', 'molar_mass','m_rho', 'formation_temperature_grad', 'kill_rate']):
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
    print("Most influential variable about max kick volume with normalizing data:", most_influential_variable_kick_volume)
    return results

    
