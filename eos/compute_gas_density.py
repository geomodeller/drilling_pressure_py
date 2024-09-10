
def compute_gas_density(z, R, temp_well_before_kick_out, kick_molar_mass, p_kick_pvt):
    """
    Calculate the gas density based on the given parameters.

    Parameters:
        z (non-dimensional): Z-factor
        R (float): The gas constant in J/mol-K.
        temp_well_before_kick_out (float): The temperature of the well before kick-out in K.
        kick_molar_mass (float): The molar mass of kick in g/mol.
        p_kick_pvt (float): The pressure at the middle of kick in psi.

    Returns:
        float: The computed gas density in ppg (pound per gallon).
    """
    return 0.05756*p_kick_pvt* kick_molar_mass/(z*R*temp_well_before_kick_out)
   