# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi)
offsets = np.linspace(0, 2*np.pi, 4, endpoint=False)
yy = np.transpose([np.sin(x + phi) for phi in offsets])
plt.rc('lines', linewidth=4)
fig, (ax0, ax1) = plt.subplots(nrows=2)
plt.rc('axes', color_cycle=['r','g','b','y'])
ax0.plot(yy)
ax0.set_title('warna umum pada siklus rgby')
ax1.set_color_cycle(['c','m','y','k'])
ax1.plot(yy)
ax1.set_title('sumbu umum pada siklus cmyk')
plt.subplots_adjust(hspace=0.3)
plt.show()
