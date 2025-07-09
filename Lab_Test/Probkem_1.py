import numpy as np 
import matplotlib.pyplot as plt

x = np.array([1,2,2,10,2,2,1])
n = len(x)

alpha_values = [0.1,0.3,0.5,0.7,0.8,0.9]

results = { }

for a in alpha_values:
    y = np.zeros(n)
    for i in range(n):
        if i == 0:
            y[i] = a * x[i]  
        else:
            y[i] = (1 - a) * y[i - 1] + a * x[i]

    results[a] = y
    
plt.figure(figsize=(12,6))

plt.plot(x,'black',label='Orginal Signal')

for a,y in results.items():
     plt.plot(y, label=f'α={a}', marker='o')


plt.title("Effect of α in differnce equation y[n] = (1-a)y[n-1] + a x[n]")
plt.xlabel('n')
plt.ylabel('y[n]')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()