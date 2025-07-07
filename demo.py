import numpy as np;
import matplotlib.pyplot as plt

n = np.arange(-10, 10)
u = np.where(n>=0, 1, 0)
plt.subplot(2,2,1)
plt.stem(n,u)
plt.title("Unit step")
plt.xlabel('n')
plt.ylabel('u')



r = np.where(n>=0, n, 0)
plt.subplot(2,2,2)
plt.stem(n,r)
plt.title("Ramp step")
plt.xlabel('n')
plt.ylabel('r')
plt.show()

