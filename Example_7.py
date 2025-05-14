import numpy as np 
import matplotlib.pyplot as plt 

x = np.array([1,3,-2,4])
y = np.array([2,3,-1,3])
z = np.array([2,-1,4,-2])

c_xy = np.correlate(x,y,'full')
c_yz = np.correlate(y,z,'full')

lag_xy = np.arange(-len(y)+1,len(x))
lag_yz = np.arange(-len(z)+1,len(y))

plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.stem(lag_xy,c_xy)
plt.title('Cross-correlation of x & y')
plt.xlabel('lag_xy')
plt.ylabel('Correlation Coefficient')
plt.grid(True)

plt.subplot(1,2,2)
plt.stem(lag_yz,c_yz)
plt.title('Cross-correlation of y & z')
plt.xlabel('lag_yz')
plt.ylabel('Correlation Coefficient')
plt.grid(True)
plt.show()