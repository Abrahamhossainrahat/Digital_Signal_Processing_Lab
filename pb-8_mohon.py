#  Filter realization using 6-point averaging, 6-point differencing equations.
import numpy as np 
import matplotlib.pyplot as plt 

n = np.linspace(0,1,200)
x = np.sin(2*np.pi * 5 * n) + 0.5*np.random.rand(len(n))

# x = np.sin(2*np.pi*5*n) + 0.5*np.random.rand(len(n))

# 6 point averaging 
def avg_filter(x):
    y = np.zeros_like(x)
    for i in range(5, len(x)):
        y[i] = (x[i] + x[i-1] + x[i-2] + x[i-3] + x[i-4] + x[i-5])/6
    return y

# 6 point differencing
def diff_filter(x):
    y = np.zeros_like(x)
    for i in range(5, len(x)):
        y[i] = (x[i] - x[i-1] + x[i-2] - x[i-3] + x[i-4] - x[i-5])/6
    return y
        
y_avg = avg_filter(x)
y_diff = diff_filter(x)

plt.figure(figsize=(12,6))

plt.subplot(3,1,1)
plt.plot(n,x,color = 'red')
plt.title('Original Signal ')
plt.xlabel('n')
plt.ylabel('x')
plt.grid(True)
plt.tight_layout(pad = 3)

plt.subplot(3,1,2)
plt.plot(n,y_avg,color = 'green')
plt.title('6 point averaging ')
plt.xlabel('n')
plt.ylabel('y_avg')
plt.grid(True)
plt.tight_layout(pad = 3)

plt.subplot(3,1,3)
plt.plot(n,y_diff, color='red')
plt.title('6 Point Differencing ')
plt.xlabel('n')
plt.ylabel('y_diff')
plt.grid(True)
plt.tight_layout(pad = 3)

plt.show()