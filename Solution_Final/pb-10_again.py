import numpy as np 
import matplotlib.pyplot as plt 

fs = 1200
t = np.arange(0,1,1/fs)
x = np.sin(2*np.pi*10*t) + 0.5*np.sin(2*np.pi*100*t)

#fIR filter 
N = 51
n = np.arange(N)
fc = 20
h = np.sinc((2*fc*(n- (N-1)/2))/fs) * np.hamming(N)
h = h/np.sum(h)
convl = np.convolve(x,h,mode='same')


plt.plot(t,x)
plt.plot(t,convl)
plt.show()