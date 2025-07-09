import numpy as np 
import matplotlib.pyplot as plt 

fs = 1200
t = np.arange(0,1,1/fs)
x = np.sin(2*np.pi*5*t) + 0.5*np.sin(2*np.pi*50*t)

# fir filter
N = 51
fc = 10
n = np.arange(N)
h = np.sinc((2*fc*(n-(N-1)/2))/fs) * np.hanning(N)
#h = np.sinc(2*fc*(n - (N-1)/2)/fs) * np.hanning(N)
h = h/np.sum(h)

filter = np.convolve(x,h, mode='same')

plt.plot(t, x, label='Original Signal')
plt.plot(t, filter, label='Filtered Signal')
plt.legend()
plt.show()