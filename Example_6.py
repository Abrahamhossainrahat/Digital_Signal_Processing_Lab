import numpy as np
import matplotlib.pyplot as plt 

def u(n):
    return np.where(n>=0,1,0)

n = np.arange(-5,20)
x = u(n)
h = u(n) - u(n-5)
y = np.convolve(x,h)  # Final output y(n)
n_y = np.arange(2*n[0], 2*n[-1] + 1)   # Final output n

plt.figure(figsize=(12,6))
plt.stem(n_y, y,'green')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title("Output of y[n] = x[n]*h[n]")
plt.grid(True)
plt.legend(loc = 'lower left')
plt.show()