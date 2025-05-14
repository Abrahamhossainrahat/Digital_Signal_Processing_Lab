import numpy as np
import matplotlib.pyplot as plt

f = 0.8
n = np.arange(-10, 10, 1)
a = 0.8

fig, axs = plt.subplots(3, 2, figsize=(10, 10))
#axs[1,1].axis('off')  # for close the specific plot

signals = {
    "Unit Step": np.where(n >= 0, 1, 0),
    "Unit Ramp": np.where(n >= 0, n, 0),
    "Exponential": pow(a,n),
    "Sine": np.sin(2*np.pi*f*n),
    "Cosine": np.cos(2*np.pi*f*n),
}


for subplt, (title, value) in zip(axs.flat, signals.items()):
  subplt.stem(n,value)
  subplt.set_title(title)
  subplt.grid(True)

plt.tight_layout()
axs[2,1].axis('off')
plt.show()