import numpy as np 
import matplotlib.pyplot as plt 

n = np.arange(0, 200)
x = np.sin(2*np.pi * 0.1 * n) + 0.5*np.random.rand(len(n))

alpha_value = [0.1, 0.2, 0.7]
filtered_signal = { }

for alpha in alpha_value:
    y = np.zeros_like(x)
    for i in range(len(n)):
        if i==0:
            y[i] = alpha * x[i]
        else:
            y[i] = (1 - alpha) * y[i - 1] + alpha * x[i]
    filtered_signal[alpha] = y
    
plt.figure(figsize=(12,6))
for a , y in filtered_signal.items():
    plt.plot(n,y, label=f'{a}')
    plt.legend(loc='lower left')

#plt.plot(n,x)
    
plt.show()