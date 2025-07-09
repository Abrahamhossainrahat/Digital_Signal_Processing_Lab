# Show that the highest rate of oscillation in a discrete-time sinusoidal is obtained when ω=π. 

import numpy as np 
import matplotlib.pyplot as plt 

def x(omega, n):
    return np.cos(omega * n)

n = np.arange(-10,10,1)

omega_1 = np.pi /4 
omega_2 = np.pi/2
omega_3 = np.pi

signal_omega_1 = x(omega_1, n)
signal_omega_2 = x(omega_2, n)
signal_omega_3 = x(omega_3, n)

plt.figure(figsize=(12,6))

#For π/4
plt.subplot(2,2,1)
plt.stem(n,signal_omega_1,linefmt='r-', basefmt='k',label='Signal_omega_1')
plt.title('Signal For π/4')
plt.xlabel('Time(n)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend(loc = 'lower left')
plt.tight_layout(pad=3)

#For π/2
plt.subplot(2,2,2)
plt.stem(n,signal_omega_2,linefmt='r-', basefmt='k',label='Signal_omega_2')
plt.title('Signal For π/2')
plt.xlabel('Time(n)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend(loc = 'lower left')
plt.tight_layout(pad=3)

#For π
plt.subplot(2,2,3)
plt.stem(n,signal_omega_3,linefmt='r-', basefmt='k',label='Signal_omega_3')
plt.title('Signal For π')
plt.xlabel('Time(n)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend(loc = 'lower left')
plt.tight_layout(pad=3)


plt.show()
