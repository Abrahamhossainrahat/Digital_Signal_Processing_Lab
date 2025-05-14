import numpy as np
import matplotlib.pyplot as plt 

def x(t):
    return 3*np.cos(200*np.pi*t) + 5*np.sin(600*np.pi*t) + 10*np.cos(1200*np.pi*t)
t = np.linspace(0,0.01,1000)
x_t = x(t)

#Frequency
fre_list = [800,1200,4000]
colors = ['r','g','b']

plt.figure(figsize=(12,6))

for i, fs in enumerate(fre_list):
    
    #Ts = 1/fs
    n = np.arange(0,0.01,1/fs)
    x_n = x(n)
    
    plt.subplot(3,1,i+1)
    plt.plot(t,x_t,'gray',label='Orginal Signal')
    plt.stem(n,x_n, linefmt=colors[i], markerfmt=colors[i], basefmt=' ', label=f'Sampling by {fs} Hz')
    plt.xlabel('Time(s)')
    plt.ylabel("Amplitude")
    plt.title(f'Sampling Rate = {fs} Hz')
    plt.legend()
    plt.grid(True)
    
plt.tight_layout()
plt.show()
    
    