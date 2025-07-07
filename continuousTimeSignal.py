import numpy as np
import matplotlib.pyplot as plt

# Time range (continuous time)
t = np.linspace(0, 1, 1000)  # 0 to 1 second, 1000 points (approx. continuous)

# Signal: Sine wave
f = 5  # frequency in Hz
x = np.sin(2 * np.pi * f * t)

# Plotting the continuous-time signal
plt.figure(figsize=(10, 5))
#plt.plot(t, x, label='x(t) = sin(2π5t)')
plt.step(t,x)
plt.title('Continuous-Time Signal')
plt.xlabel('Time (t) in seconds')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
