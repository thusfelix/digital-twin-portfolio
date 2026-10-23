import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 500)
plt.plot(t, np.sin(2 * np.pi * 2 * t))
plt.xlabel("Time (s)")
plt.ylabel("Displacement")
plt.title("Phase 0 test: 2 Hz sine wave")
plt.show()