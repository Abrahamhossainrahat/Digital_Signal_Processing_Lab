# Consider the continuous-time analog signal x(t)=3cos(100πt). Sample the analog 
# signal at 200 Hz and 75 Hz. Show the discrete-time signal after sampling. ⟹ 
# realization.  

import numpy as np 
import matplotlib.pyplot as plt 

def x(t):
    return 3 * np.cos(100 * np.pi * t)

#Orginal Signal 
t = np.linspace(0, 0.05, 1000)
orginal_signal = x(t)

#Sampling by 200 Hz 
ts1 = 200
n_200 = np.arange(0,0.05,1/ts1)
sampling_200 = x(n_200)

#Sampling by 75 Hz 
ts1 = 75
n_75 = np.arange(0,0.05,1/ts1)
sampling_75 = x(n_75)

plt.figure(figsize=(12,6))

plt.subplot(2,2,1)
plt.plot(t,orginal_signal,color='red' ,label = 'Orginal_Signal')
plt.title('Orginal Signal')
plt.xlabel('Time(t)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend(loc = 'lower left')
plt.tight_layout(pad = 3)

#Samoling by 200 Hz
plt.subplot(2,2,2)
plt.plot(t,orginal_signal,color='red' ,label = 'Orginal_Signal')
plt.stem(n_200, sampling_200, linefmt='g-', basefmt='k', label='sampling 200 Hz')
plt.title('Sampling by 200 Hz')
plt.xlabel('Time(n_200)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend(loc = 'lower left')
plt.tight_layout(pad = 3)

#Samoling by 75 Hz
plt.subplot(2,2,3)
plt.plot(t,orginal_signal,color='red' ,label = 'Orginal_Signal')
plt.stem(n_75, sampling_75, linefmt='g-', basefmt='k', label='sampling 75 Hz')
plt.title('Sampling by 75 Hz')
plt.xlabel('Time(n_75)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend(loc = 'lower left')
plt.tight_layout(pad = 3)

plt.show()