import numpy as np

from scripts.ssd_core import SSDParameters, sigma, a_eff, H


def test_sigma_positive():
    t = np.linspace(0.1, 2.0, 100)
    params = SSDParameters(A=1.0, B=1.0)
    s = sigma(t, params)
    assert np.all(s > 0)


def test_aeff_positive():
    t = np.linspace(0.1, 2.0, 100)
    params = SSDParameters(A=1.0, B=1.0)
    a = a_eff(t, params)
    assert np.all(a > 0)


def test_H_finite():
    t = np.linspace(0.1, 2.0, 100)
    params = SSDParameters(A=1.0, B=1.0)
    h = H(t, params)
    assert np.all(np.isfinite(h))
