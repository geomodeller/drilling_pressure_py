
def compute_gas_density(z, R, temp_well_before_kick_out, molar_mass_methane, p_k_z):
    """
    Calculate the gas density based on the given parameters.

    Parameters:
        z (float): Z-factor
        R (float): The gas constant in J/mol-K.
        temp_well_before_kick_out (float): The temperature of the well before kick-out in Kelvin.
        molar_mass_methane (float): The molar mass of methane in g/mol.
        p_k_z (float): The pressure at the kick-out point in psi.

    Returns:
        float: The computed gas density in ppg (pound per gallon).
    """
    return 0.05756*p_k_z* molar_mass_methane/(z*R*temp_well_before_kick_out)
   