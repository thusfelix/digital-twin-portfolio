import numpy as np
import matplotlib.pyplot as plt

m, k = 20.0, 50_000.0     # kg, N/m
x0, v0 = 0.01, 0.0        # initial displacement (m), velocity (m/s)

wn = np.sqrt(k / m)
c_crit = 2 * np.sqrt(k * m)
t = np.linspace(0, 1.0, 2000)

def free_response(zeta, t):
    if zeta < 1:                      # under-damped
        wd = wn * np.sqrt(1 - zeta**2)
        return np.exp(-zeta * wn * t) * (
            x0 * np.cos(wd * t)
            + (v0 + zeta * wn * x0) / wd * np.sin(wd * t))
    elif zeta == 1:                   # critically damped
        return np.exp(-wn * t) * (x0 + (v0 + wn * x0) * t)
    else:                             # over-damped
        r = wn * np.sqrt(zeta**2 - 1)
        s1, s2 = -zeta * wn + r, -zeta * wn - r
        C2 = (v0 - s1 * x0) / (s2 - s1)
        C1 = x0 - C2
        return C1 * np.exp(s1 * t) + C2 * np.exp(s2 * t)

for zeta in [0.1, 0.5, 1.0, 2.0]:
    plt.plot(t, free_response(zeta, t) * 1000, label=f"ζ = {zeta}")

plt.xlabel("Time (s)")
plt.ylabel("Displacement (mm)")
plt.title("Free vibration: effect of damping ratio")
plt.legend()
plt.grid(True)
plt.savefig("1A/free_response.png", dpi=150)
plt.show()
