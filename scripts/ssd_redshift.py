import numpy as np

from scripts.ssd_core import SSDParameters, a_eff


def redshift_from_aeff(a):
    """
    Convert effective scale factor to redshift:
    z = 1/a - 1
    """
    return (1.0 / a) - 1.0


def z_of_t(t, params):
    """
    Compute redshift as a function of t
    using the SSD effective scale factor.
    """
    a = a_eff(t, params)
    return redshift_from_aeff(a)


if __name__ == "__main__":
    t = np.linspace(0.1, 2.0, 10)
    params = SSDParameters()

    z = z_of_t(t, params)
    print("z(t) sample:", z)
