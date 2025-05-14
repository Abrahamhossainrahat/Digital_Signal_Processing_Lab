import numpy as np 
import matplotlib.pyplot as plt 

def x(t):
    return 3* np.cos(100 * np.pi * t )
#Analog Signal
t = np.linspace(0,0.05,1000)
x_t = x(t)

# No alaising 
fs1 = 200
ts1 = 1/fs1
n1 = np.arange(0,0.05,ts1)
x1 = x(n1)

#Alaising 
fs2 = 75
ts2 = 1/fs2
n2 = np.arange(0,0.05, ts2)
x2 = x(n2)

plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.plot(t,x_t, label= "Analog Signal")
plt.stem(n1,x1,linefmt='r-',markerfmt='go' ,basefmt=' ',label='Sampled 200 hz')
plt.title('Sampling at 200 Hz (No Aliasing)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()


plt.subplot(1,2,2)
plt.plot(t,x_t, label= "Analog Signal")
plt.stem(n2,x2,linefmt='g-', markerfmt='ro',basefmt=' ', label='Sampling @75H')
plt.title("Sampling at 75Hz (Alaiasing)")
plt.xlabel('Time (s)')
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()