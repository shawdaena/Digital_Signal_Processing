'''  Consider the continuous-time analog signal x(t)=3cos(100πt). Sample the analog 
signal at 200 Hz and 75 Hz. Show the discrete-time signal after sampling. ⟹ 
realization. '''

import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(0,0.1,1000)
input = 3*np.cos(100*np.pi*n)
plt.subplot(2,2,1)
plt.plot(n,input, label='Given signal')
plt.legend()

n1 = np.arange(0,0.1,1/200)
input1 = 3*np.cos(100*np.pi*n1)
plt.subplot(2,2,2)
plt.plot(n,input, 'lightgray')
plt.stem(n1, input1,'r', label='200Hz frequence signal')
plt.legend(loc='lower right')

n2 = np.arange(0,0.1,1/75)
input2 = 3*np.cos(100*np.pi*n2)
plt.subplot(2,2,3)
plt.plot(n,input, 'lightgray')
plt.stem(n2, input2,'g', label='75 Hz frequence signal')
plt.legend(loc = 'lower right')
plt.show()








'''
Consider the continuous-time analog signal x(t)=3cos(100πt). Sample the analog 
signal at 200 Hz and 75 Hz. Show the discrete-time signal after sampling. ⟹ 
realization. 
'''
'''
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(0,0.04, 1000)
y = 3*np.cos(100*np.pi*n)

plt.plot(n, y, label = 'Input Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

n = np.arange(0,0.04, 1/75)
y = 3*np.cos(100*np.pi*n)

plt.stem(n, y, 'g', label='sampled 75')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

n = np.arange(0,0.04, 1/200)
y = 3*np.cos(100*np.pi*n)

plt.stem(n, y, 'r', label='sampled 100')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
'''