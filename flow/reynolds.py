
def reynolds(mud_density, vel, mu_a, d1, d2, openhole, is_annulus = True):
    """
    Calculate the Reynolds number based on the given parameters.

    Parameters:
        mud_density (float): The mass density of the fluid in ppg
        vel (float): The velocity of the fluid in ft/s
        mu_a (float): The dynamic viscosity of the fluid in cp
        d1 (float): The inner diameter of the pipe in inch
        d2 (float, optional): The outer diameter of the pipe in inch. Defaults to None.
        openhole (float): The diameter of openhole in inch.
        is_annulus (bool, optional): Flag indicating if the pipe is an annulus. Defaults to True.

    Returns:
        float: The Reynolds number.


    Notes:
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
        return 928* 0.816 * mud_density*vel*(openhole - d2)/mu_a
    else:
        return 928 * mud_density*vel*(d1)/mu_a
       