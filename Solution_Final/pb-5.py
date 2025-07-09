# Consider the analog signal: xa(t)=3cos(200πt)+5sin(600πt)+10cos(1200πt). 
# Show the effect of sampling rate.  

import numpy as np 
import matplotlib.pyplot as plt 

def x(t):
    return (3 * np.cos(200 * np.pi * t)) + (5* np.sin(600 * np.pi * t)) + (10 * np.cos(1200 * np.pi * t))

#Orginal Signal
t = np.linspace(0,0.01, 1000)
orginal_signal = x(t)

#Sampling by different Frequency 
fre_list = [800, 1000, 4000]
colors = ['r', 'g', 'b']

plt.figure(figsize=(12,6))

# #Original Signal
# plt.subplot(2,2,1)
# plt.plot(t,orginal_signal,label = 'orginal_signal')
# plt.title('Orginal Signal')
# plt.xlabel('Time(t)')
# plt.ylabel('Amplitude')
# plt.grid(True)
# plt.legend(loc = 'lower left')
# plt.tight_layout(pad = 3)

#Sampling by different frequency
for i, frequency in enumerate(fre_list):
    n = np.arange(0,0.01,1/frequency)
    sampling_signal = x(n)
    plt.subplot(3,1,i+1)
    plt.plot(t,orginal_signal,label = 'orginal_signal')
    plt.stem(n, sampling_signal, linefmt=colors[i], basefmt='k',label=f'Sampling {frequency} Hz')
    plt.title(f'Sampling by {frequency} Hz')
    plt.xlabel('Time(n)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend(loc = 'lower left')
    plt.tight_layout(pad = 3)


plt.show()