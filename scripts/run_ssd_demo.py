import os
import numpy as np
import matplotlib.pyplot as plt

from ssd_core import SSDParameters, sigma, a_eff, H


def main():
    t = np.linspace(0.1, 2.0, 200)
    params = SSDParameters(A=1.0, B=1.0)

    s = sigma(t, params)
    a = a_eff(t, params)
    h = H(t, params)

    os.makedirs("results", exist_ok=True)

    plt.figure(figsize=(8, 5))
    plt.plot(t, s, label="sigma(t)")
    plt.plot(t, a, label="a_eff(t)")
    plt.plot(t, h, label="H(t)")
    plt.xlabel("t")
    plt.ylabel("value")
    plt.title("SSD demo")
    plt.legend()
    plt.tight_layout()
    plt.savefig("results/ssd_demo_plot.png", dpi=150)
    plt.close()

    print("Saved: results/ssd_demo_plot.png")


if __name__ == "__main__":
    main()
