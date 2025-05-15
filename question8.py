'''
Filter realization using 6-point averaging, 6-point differencing equations. 
'''

import numpy as np
import matplotlib.pyplot as plt

def six_point_averaging(signal):
    output = np.zeros(len(signal))
    for n in range(len(signal)):
        if n < 5: 
            output[n] = signal[n]
        else:
            output[n] = (signal[n] + signal[n-1] + signal[n-2] +
                        signal[n-3] + signal[n-4] + signal[n-5]) / 6.0
    return output

def six_point_differencing(signal):
    output = np.zeros(len(signal))
    for n in range(len(signal)):
        if n < 5:  
            output[n] = signal[n]
        else:
            output[n] = (signal[n] - signal[n-5]) / 6.0
    return output


t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 50 * t)


averaged_signal = six_point_averaging(signal)
differenced_signal = six_point_differencing(signal)


plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, signal, label='Original Signal')
plt.title('Original Signal')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, averaged_signal, label='6-Point Averaging', color='green')
plt.title('6-Point Averaging Filter (Low-Pass)')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, differenced_signal, label='6-Point Differencing', color='red')
plt.title('6-Point Differencing Filter (High-Pass)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()