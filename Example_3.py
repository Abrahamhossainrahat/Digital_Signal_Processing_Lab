import numpy as np 
import matplotlib.pyplot as plt 

def x(n,omega):
    return np.cos(omega * n)

n = np.arange(-10,10,1)
omega1 = np.pi/4
omega2 = np.pi/2
omega3 = np.pi 

x1 = x(n,omega1)
x2 = x(n,omega2)
x3 = x(n,omega3)

plt.figure(figsize=(12,12))
plt.subplot(3,2,1)
plt.stem(n,x1,linefmt='r-', markerfmt='go')
plt.xlabel('n')
plt.ylabel('x1(n)')
plt.title('For pi/4')
plt.legend()

plt.subplot(3,2,2)
plt.stem(n,x2,linefmt='g-', markerfmt='ro')
plt.xlabel('n')
plt.ylabel('x2(n)')
plt.title('For pi/2')
plt.legend()

plt.subplot(3,2,3)
plt.stem(n,x3,linefmt='y-', markerfmt='go')
plt.xlabel('n')
plt.ylabel('x3(n)')
plt.title('For pi')
plt.legend()
plt.show()