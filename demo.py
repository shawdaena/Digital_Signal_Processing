import numpy as np
import matplotlib.pyplot as plt

def six_point_averaging(signal):
    output = np.zeros(len(signal))
    
    for n in range (len(signal)):
        if n<5:
            output[n] = signal[n]
        else:
            output[n] = (signal[n]+signal[n-1]+signal[n-2]+signal[n-3]+signal[n-4]+signal[n-5])/6.0
            
    return output

def six_point_differencing(signal):
    output = np.zeros(len(signal))
    
    for n in range (len(signal)):
        if n<5:
            output[n] = signal[n]
        else:
            output[n] = (signal[n] - signal[n-5])/6.0
            
    return output

t = np.linspace(0,1,1000)
signal = np.sin(2*np.pi*5*t) + 0.5* np.sin(2*np.pi*50*t)

Averaging = six_point_averaging(signal)
Differencing = six_point_differencing(signal)

plt.subplot(3,2,1)
plt.plot(t, signal)
plt.grid()
plt.legend()

plt.subplot(3,2,2)
plt.plot(t, Averaging)
plt.grid()
plt.legend()

plt.subplot(3,2,3)
plt.plot(t, Differencing)
plt.grid()
plt.legend()
plt.show()