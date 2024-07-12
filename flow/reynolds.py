
def reynolds(m_rho, vel, mu_a, d1, d2 = None, is_annulus = True):
    """
    Calculate the Reynolds number based on the given parameters (choe, 2017).

    Parameters:
        m_rho (float): The mass density of the fluid in ppg
        vel (float): The velocity of the fluid in ft/s
        mu_a (float): The dynamic viscosity of the fluid in cp
        d1 (float): The inner diameter of the pipe in inch
        d2 (float, optional): The outer diameter of the pipe in inch. Defaults to None.
        is_annulus (bool, optional): Flag indicating if the pipe is an annulus. Defaults to True.

    Returns:
        float: The Reynolds number.


    Notes:
        - If `d2` is greater than `d1`, the function swaps the values of `d1` and `d2`.
        - The function calculates the Reynolds number based on the given parameters.
        - The formula used to calculate the Reynolds number depends on the value of `is_annulus`.
        - If `is_annulus` is True, the function calculates the Reynolds number for an annular pipe.
        - If `is_annulus` is False, the function calculates the Reynolds number for a cylindrical pipe.

    Examples:
        >>> reynolds(1000, 10, 0.01, 0.1, 0.2, is_annulus=True)
        _____
        >>> reynolds(1000, 10, 0.01, 0.2, 0.1, is_annulus=True)
        _____
        >>> reynolds(1000, 10, 0.01, 0.1, is_annulus=False)
        _____
    """
    if is_annulus:
        if d2 > d1:
            d1, d2 = d2, d1
        assert d2 is not None, 'd2 is not input properly'
        return 928* 0.816 * m_rho*vel*(d2 - d1)/mu_a
    else:
        return 928 * m_rho*vel*(d1)/mu_a
       