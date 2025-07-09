import numpy as np 
import matplotlib.pyplot as plt 

n = np.arange(-10,10,1)

#Unite Step 
u = np.where(n>=0,1,0)
ur = np.where(n>=0, n,0)
a = 0.8
e = np.pow(a,n)
f = 200
sin = np.sin(2 * np.pi * f * n)
cos = np.cos(2 * np.pi * f * n)
plt.figure(figsize=(12,8))

plt.subplot(3,2,1)
plt.stem(n,u)

plt.subplot(3,2,2)
plt.stem(n,ur)

plt.subplot(3,2,3)
plt.stem(n,e)

plt.subplot(3,2,4)
plt.stem(n,sin)

plt.subplot(3,2,5)
plt.stem(n,cos)

plt.show()