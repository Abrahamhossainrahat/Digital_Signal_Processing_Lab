import numpy as np
import matplotlib.pyplot as plt

#clean
n = np.arange(0, 200)
frequency = 0.1
clean_signal = np.sin(2 * np.pi * frequency * n)
  
#clean+noise
np.random.seed(42)
noise = np.random.normal(0, 0.5, size=n.shape)
noisy_signal = clean_signal + noise

#filter
alpha_values = [0.1,0.3,0.6]
colors = ['r','y','b']
filtered_signals = {}

for a in alpha_values:
    y = np.zeros_like(noisy_signal)
    for i in range(len(n)):
        if i == 0:
            y[i] = a * noisy_signal[i]
        else:
            y[i] = (1 - a) * y[i - 1] + a * noisy_signal[i]
    filtered_signals[a] = y

plt.figure(figsize=(14, 7))

plt.plot(n, clean_signal, label='Clean Signal', linewidth=2, color='black')
plt.plot(n, noisy_signal, label='Noisy Signal',color='green')
i=0
for alpha, y in filtered_signals.items():
    plt.plot(n, y, label=f'Filtered Signal (α = {alpha})', linewidth=2,color=colors[i] )
    i=i+1

plt.title('Clean vs Noisy vs Filtered Signals (All in One Plot)')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()