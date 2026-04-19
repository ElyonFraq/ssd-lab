import numpy as np

from scripts.ssd_core import SSDParameters, a_eff
from scripts.ssd_redshift import redshift_from_aeff, z_of_t


def test_redshift_from_aeff_finite():
    a = np.array([1.0, 1.1, 1.2, 1.3])
    z = redshift_from_aeff(a)
    assert np.all(np.isfinite(z))


def test_z_of_t_finite():
    t = np.linspace(0.1, 2.0, 100)
    params = SSDParameters(A=1.0, B=1.0)
    z = z_of_t(t, params)
    assert np.all(np.isfinite(z))


def test_z_matches_aeff_definition():
    t = np.linspace(0.1, 2.0, 100)
    params = SSDParameters(A=1.0, B=1.0)

    a = a_eff(t, params)
    z1 = redshift_from_aeff(a)
    z2 = z_of_t(t, params)

    assert np.allclose(z1, z2)
