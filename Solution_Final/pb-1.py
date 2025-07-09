# Generating elementary signals like Unit Step, Ramp, Exponential, Sine, and Cosine sequences.  

import numpy as np 
import matplotlib.pyplot as plt

def x(t):
    return np.sin(2*np.pi * 100 * t)

n = np.arange(-10,10,1)
unit_step = np.where(n>=0, 1, 0)
unit_ramp = np.where(n>=0, n, 0)
a = 0.8      #Let a = 0.2 For Exponential 
exponential = np.pow(a,n)
f = 0.2     
sin_wave = np.sin(2 * np.pi * f * n)
cos_wave = np.cos(2 * np.pi * f * n)


plt.figure(figsize=(12,6))
#Unite Step
plt.subplot(3,2,1)
plt.stem(n, unit_step,linefmt='r-',markerfmt='go',basefmt='k',label = 'Unite_step')
plt.title("Unite Step")
plt.xlabel("Time(n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend(loc = 'lower left')
plt.tight_layout(pad= 3)

#Unite Ramp
plt.subplot(3,2,2)
plt.stem(n, unit_ramp,linefmt='g-',markerfmt='ro',basefmt='k',label = 'Unite_Ramp')
plt.title("Unite Ramp")
plt.xlabel("Time(n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend(loc = 'lower left')
plt.tight_layout(pad= 3)

#Exponential 
plt.subplot(3,2,3)
plt.stem(n, exponential,linefmt='g-',markerfmt='ro',basefmt='k',label = 'Exponential')
plt.title("Exponential")
plt.xlabel("Time(n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend(loc = 'lower left')

#sin Wave 
plt.subplot(3,2,4)
plt.plot(n,sin_wave)
plt.stem(n, sin_wave,linefmt='g-',markerfmt='ro',basefmt='k',label = 'Sin_Wave')
plt.title("Sin Wave")
plt.xlabel("Time(n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend(loc = 'lower left')
plt.tight_layout(pad= 3)

#cos wave 
plt.subplot(3,2,5)
plt.plot(n,cos_wave)
plt.stem(n, cos_wave,linefmt='g-',markerfmt='ro',basefmt='k',label = 'Cos_Wave')
plt.title("Cos Wave")
plt.xlabel("Time(n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend(loc = 'lower left')
plt.tight_layout(pad= 3)

plt.show()
