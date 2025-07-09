#  Filter realization using 6-point averaging, 6-point differencing equations.

import numpy as np 
import matplotlib.pyplot as plt 

x = np.array([0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 5, 0, 0, 0])
n = np.arange(len(x))

avg_flt = np.ones(6)/6

low_pass = np.convolve(x,avg_flt, mode='same')

x_paded = np.concatenate((np.zeros(6),x))
high_pass = x_paded[6:] - x_paded[:-6]
high_pass = high_pass[:len(x)]




plt.figure(figsize=(12,6))

plt.subplot(3,1,1)
plt.stem(n,x)

plt.subplot(3,1,2)
plt.stem(n,low_pass)

plt.subplot(3,1,3)
plt.stem(n,high_pass)
plt.show()
