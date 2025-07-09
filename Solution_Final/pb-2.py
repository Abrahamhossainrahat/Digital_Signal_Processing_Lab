# Demonstrates the effect of sampling, aliasing.  

import numpy as np 
import matplotlib.pyplot as plt 

def x(t):
    return np.cos( np.pi * 100 * t)

#Orginal Signal
t = np.linspace(0, 0.05, 1000)
orginal_signal = x(t)

#No Alaising 
fs1 = 200
n1= np.arange(0,0.05,1/fs1)
Sampling_Signal_1 = x(n1)

#Alaising 
fs2 = 75
n2= np.arange(0,0.05,1/fs2)
Sampling_Signal_2 = x(n2)

#Orginal Signal
plt.figure(figsize=(12,6))
plt.subplot(2,2,1)
plt.plot(t,orginal_signal,color = 'red' ,label = "Orginal Signal")
plt.title("Orginal Signal")
plt.xlabel("Time(t)")
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend(loc = 'lower left')
plt.tight_layout(pad=3)

#No Alaising Signal 
plt.subplot(2,2,2)
plt.plot(t,orginal_signal,color = 'red' ,label = "Orginal Signal")
plt.stem(n1,Sampling_Signal_1, linefmt='g-', basefmt='k', label='Sampling 200 Hz')
plt.title("Sampling by 200Hz(No Alaising)")
plt.xlabel("Time(n1)")
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend(loc = 'lower left')
plt.tight_layout(pad=3)

#Alaising Signal 
plt.subplot(2,2,3)
plt.plot(t,orginal_signal,color = 'red' ,label = "Orginal Signal")
plt.stem(n2,Sampling_Signal_2, linefmt='g-', basefmt='k', label='Sampling 75 Hz')
plt.title("Sampling by 75Hz(Alaising)")
plt.xlabel("Time(n2)")
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend(loc = 'lower left')
plt.tight_layout(pad=3)

plt.show()