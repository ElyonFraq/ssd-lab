import numpy as np

from scripts.ssd_core import H
from scripts.ssd_redshift import z_of_t


def H_of_z(t, params):
    """
    Compute H as a function of z via the parametric mapping t -> z(t).
    Returns arrays (z, H).
    """
    z = z_of_t(t, params)
    h = H(t, params)
    return z, h


def sort_by_z(z, h):
    """
    Sort paired arrays by increasing z.
    """
    idx = np.argsort(z)
    return z[idx], h[idx]


if __name__ == "__main__":
    from scripts.ssd_core import SSDParameters

    t = np.linspace(0.1, 2.0, 100)
    params = SSDParameters()

    z, h = H_of_z(t, params)
    z, h = sort_by_z(z, h)

    print("z sample:", z[:5])
    print("H(z) sample:", h[:5])
