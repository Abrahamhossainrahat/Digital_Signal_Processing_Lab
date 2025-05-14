import numpy as np 
import matplotlib.pyplot as plt 

def x(t):
    return 3*np.cos(100*np.pi*t)

t = np.linspace(0,0.05,1000)
x_t = x(t)

#Sampling by 200 Hz
fs1 = 200
n1 = np.arange(0,0.05,1/fs1)
x_n1 = x(n1)

#Sampling by 75 Hz
fs2 = 75
n2 = np.arange(0,0.05,1/fs2)
x_n2 = x(n2)

# Show
plt.figure(figsize=(12,6))
plt.plot(t, x_t, 'black', label = 'Orginal Signal')
plt.stem(n1, x_n1, linefmt='r-',markerfmt='ro', basefmt=' ', label='Sampling by 200HZ')
plt.stem(n2, x_n2, linefmt='g-',markerfmt='go', basefmt=' ', label='Sampling by 75HZ')
# offset = 0.0005  # small time shift
# markerline1, stemlines1, baseline1 = plt.stem(n1 - offset, x_n1, linefmt='r', markerfmt='ro', basefmt=' ')
# markerline1.set_label('Sampling by 200HZ')

# # Green points (75 Hz)
# markerline2, stemlines2, baseline2 = plt.stem(n2 + offset, x_n2, linefmt='g', markerfmt='go', basefmt=' ')
# markerline2.set_label('Sampling by 75HZ')
plt.grid(True)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.title('Sampling of x(t) = 3cos(100πt)')
plt.legend(loc = 'lower left')
plt.show()