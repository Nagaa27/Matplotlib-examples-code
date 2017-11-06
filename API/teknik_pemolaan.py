# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import EngFormatter

fig, ax = plt.subplots()
ax.set_xscale('log')
formatter = EngFormatter(unit='Hz', places=1)
ax.xaxis.set_major_formatter(formatter)

#jika ingin mengubah nilai dan keadaan dari tampilan
xs = np.logspace(1, 9, 100)
ys = (0.8 + 0.4 * np.random.uniform(size=100)) * np.log10(xs) **2
ax.plot(xs, ys)

plt.show()
