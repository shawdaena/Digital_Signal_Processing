'''Consider the analog signal: xa(t)=3cos(200πt)+5sin(600πt)+10cos(1200πt). 
Show the effect of sampling rate. '''

import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(0,0.01,1000)
input = 3*np.cos(200*np.pi*n) + 5*np.sin(600*np.pi*n) + 10*np.cos(1200*np.pi*n)

plt.subplot(2,2,1)
plt.plot(n, input)
plt.title("Signal")
plt.xlabel("N")
plt.ylabel("input")

n1 = np.arange(0,0.01,1/800)
input1 = 3*np.cos(200*np.pi*n1) + 5*np.sin(600*np.pi*n1) + 10*np.cos(1200*np.pi*n1)
plt.subplot(2,2,2)
plt.plot(n, input, 'lightgray')
plt.stem(n1, input1, label = 'sampled of low of nyquest')
plt.title("low Nyquest rate")
plt.legend()

n2 = np.arange(0,0.01,1/1200)
input2 = 3*np.cos(200*np.pi*n2) + 5*np.sin(600*np.pi*n2) + 10*np.cos(1200*np.pi*n2)
plt.subplot(2,2,3)
plt.plot(n, input, 'lightgray')
plt.stem(n2, input2, label = 'sampled of nyquest')
plt.title("Nyquest rate")
plt.legend()

n3 = np.arange(0,0.01,1/2000)
input3 = 3*np.cos(200*np.pi*n3) + 5*np.sin(600*np.pi*n3) + 10*np.cos(1200*np.pi*n3)
plt.subplot(2,2,4)
plt.plot(n, input, 'lightgray')
plt.stem(n3, input3, label = 'sampled of high of nyquest')
plt.title("high Nyquest rate")
plt.legend()
plt.tight_layout()
plt.show()













'''
Consider the analog signal: xa(t)=3cos(200πt)+5sin(600πt)+10cos(1200πt). 
Show the effect of sampling rate.  

'''
'''import numpy as np
import matplotlib.pyplot as plt

n = n1 = np.linspace(0, 0.01, 800)


input_signal = 3 * np.cos(200*np.pi*n) + 5*np.sin(600*np.pi*n) + 10*np.cos(1200*np.pi*n)
plt.subplot(4,1,1)
plt.plot(n, input_signal)
plt.grid(True)


n = np.arange(0,0.01,1/800)
low_sampled = 3 * np.cos(200*np.pi*n) + 5*np.sin(600*np.pi*n) + 10*np.cos(1200*np.pi*n)
plt.subplot(4,1,2)
plt.plot(n1, input_signal, 'lightgray')
plt.stem(n, low_sampled, label = 'sampled of low of nyquest')
plt.grid(True)

n = np.arange(0,0.01,1/1200)
low_sampled = 3 * np.cos(200*np.pi*n) + 5*np.sin(600*np.pi*n) + 10*np.cos(1200*np.pi*n)
plt.subplot(4,1,3)
plt.plot(n1, input_signal, 'lightgray')
plt.stem(n, low_sampled, label = 'sampled of nyquest')
plt.grid(True)
plt.legend()

n = np.arange(0,0.01,1/2000)
low_sampled = 3 * np.cos(200*np.pi*n) + 5*np.sin(600*np.pi*n) + 10*np.cos(1200*np.pi*n)
plt.subplot(4,1,4)
plt.plot(n1, input_signal, 'lightgray')
plt.stem(n, low_sampled, label = 'sampled of high nyquest')
plt.grid(True)

plt.legend()
plt.tight_layout()
plt.show()

'''