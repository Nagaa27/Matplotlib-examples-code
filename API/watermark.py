# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(np.random.rand(20), '-o', ms=20, lw=2, alpha=0.7, mfc='orange')
ax.grid()

#ukuran huruf, jenis font serta warna dan posisi
fig.text(0.95, 0.05, 'Matius Celcius Sinaga',
		fontsize =50, color='gray',
		ha='right', va='bottom', alpha=0.5)
plt.show()

