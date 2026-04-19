import numpy as np


class SSDParameters:
    """
    Container for SSD model parameters.
    Extend later if needed.
    """
    def __init__(self, A=1.0, B=1.0):
        self.A = A
        self.B = B


def Se(t, params):
    """
    Extraction component (Se).
    Placeholder definition.
    """
    return params.A * np.ones_like(t)


def Sa(t, params):
    """
    Expansion component (Sa).
    Placeholder definition.
    """
    return params.B * (1 + t)


def sigma(t, params):
    """
    Core SSD relation:
    σ(t) = Se(t) * Sa(t)
    """
    return Se(t, params) * Sa(t, params)


def a_eff(t, params):
    """
    Effective scale factor:
    a_eff = σ^(1/3)
    """
    return sigma(t, params) ** (1.0 / 3.0)


def H(t, params):
    """
    H(t) = (1/3) * (σ̇ / σ)
    Numerical derivative.
    """
    s = sigma(t, params)
    ds_dt = np.gradient(s, t)
    return (1.0 / 3.0) * (ds_dt / s)


if __name__ == "__main__":
    # simple test run

    t = np.linspace(0.1, 2.0, 100)
    params = SSDParameters()

    s = sigma(t, params)
    a = a_eff(t, params)
    h = H(t, params)

    print("sigma(t) sample:", s[:5])
    print("a_eff(t) sample:", a[:5])
    print("H(t) sample:", h[:5])
