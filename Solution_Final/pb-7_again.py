#  Given x(n)=[1,3,−2,4] y(n)=[2,3,−1,3] z(n)=[2,−1,4,−2] 
# Find the correlation between x(n) & y(n) and y(n) & z(n). ⟹ observe the 
# realization.

import numpy as np 
import matplotlib.pyplot as plt 

x = np.array([1,3,-2,4])
y = np.array([2,3,-1,3])
z = np.array([2,-1,4,-2])

# Correlation 
xy = np.correlate(x,y,'full')
yz = np.correlate(y,z,'full')

lag_xy = np.arange(-len(y)+1, len(x))
lag_yz = np.arange(-len(z)+1, len(y))

plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.stem(lag_xy, xy,linefmt='r-', basefmt='k', label='correlation xy')
plt.title('Correlation of xy')
plt.xlabel('lag_xy')
plt.ylabel('xy')
plt.grid(True)
plt.legend(loc = 'lower left')
plt.tight_layout(pad = 3)

plt.subplot(1,2,2)
plt.stem(lag_yz, yz,linefmt='g-', basefmt='k', label='correlation yz')
plt.title('Correlation of yz')
plt.xlabel('lag_yz')
plt.ylabel('yz')
plt.grid(True)
plt.legend(loc = 'lower left')
plt.tight_layout(pad = 3)

plt.show()

