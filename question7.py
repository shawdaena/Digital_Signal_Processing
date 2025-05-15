'''
Given x(n)=[1,3,−2,4] y(n)=[2,3,−1,3] z(n)=[2,−1,4,−2] 
Find the correlation between x(n) & y(n) and y(n) & z(n). ⟹ observe the 
realization. 
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,3,-2,4])
y = np.array([2,3,-1,3])
z = np.array([2,-1,4,-2])

def correlation(x,y):
    numerotor = sum(x*y)
    denominator = np.sqrt(np.sum(x**2)) * np.sqrt(np.sum(y**2))
    return numerotor/denominator

def Cal_correlation(x,y):
    N = len(x)+len(y)-1
    result = np.zeros(N)
    
    for i in range(N):
        sum = 0
        for k in range(len(x)):
            if i-k>=0 and i-k< len(y):
                sum += x[k]*y[i-k]
        result[i] = sum
        
    return result

r_xy = correlation(x,y)
r_yz = correlation(y,z)

s = str(r_xy)
s = 'correlation value: ' + s[:5]

r_xy_0 = Cal_correlation(x, y[::-1])
r_yz_0 = Cal_correlation(y, z[::-1])
lag = np.arange(-len(x) + 1, len(y))

plt.subplot(2, 1, 1)
plt.title('Correlation between x(n) and y(n)')
plt.stem(lag , r_xy_0, label= s, linefmt='b-', basefmt='k-')
plt.legend()
plt.xlabel('Lag')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()