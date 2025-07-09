#  The impulse response of a discrete-time LTI system is h(n)={u(n)−u(n−5)}. 
# Determine the output of the system for the input x[n]=u(n), using the convolution 
# sum.

import numpy as np 
import matplotlib.pyplot as plt 

def u(n):
    return np.where(n>=0, 1, 0)

n = np.arange(-5,20)
x = u(n)
h = u(n) - u(n-5)

convolution_y = np.convolve(x,h)

range_n = np.arange(2*n[0], 2*n[-1] + 1)

plt.figure(figsize=(12,6))
plt.stem(range_n, convolution_y,linefmt='r-', markerfmt='go', basefmt='k', label='y = x(n)*h(n)')
plt.title('Convolution')
plt.xlabel('range_n')
plt.ylabel('y = x(n)*h(n)')
plt.grid(True)
plt.legend(loc = 'lower right')
plt.show()

