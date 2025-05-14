import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 10)  # time indices
u = np.where(n >= 0, 1, 0)  # unit step definition
plt.subplot(5,1,1)
plt.stem(n, u)
plt.title('Unit Step Sequence')
plt.xlabel('n')
plt.ylabel('u[n]')
#plt.grid()

r = np.where(n >= 0, n, 0)  # ramp is 0 for n<0, linearly increasing for n>=0

plt.subplot(5,2,1)
plt.stem(n, r)
plt.title('Ramp Sequence')
plt.xlabel('n')
plt.ylabel('r[n]')
plt.grid()
plt.show()
