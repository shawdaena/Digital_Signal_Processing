import numpy as np
import matplotlib.pyplot as plt

# Discrete time indices
n = np.arange(0, 20, 1)  # n = 0, 1, 2, ..., 19

# Signal: Discrete Sine wave
f = 0.1  # frequency in Hz
x = np.sin(2 * np.pi * f * n)

# Plotting the discrete-time signal
plt.figure(figsize=(10, 5))
plt.stem(n, x)
plt.title('Discrete-Time Signal')
plt.xlabel('Discrete Time index n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
