# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as collections

t= np.arange(0.0, 1, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = 1.2*np.sin(4*np.pi*t)
fig, ax = plt.subplots()
ax.set_title('bendera_indonesia')
ax.plot(t, s1, color='black')
ax.axhline(0, color='black', lw=1)

#diambil dari dasar bendera spanyol
collection = collections.BrokenBarHCollection.span_where(
       t, ymin=0, ymax=1, where=s1>-2, facecolor='red', alpha=1)
ax.add_collection(collection)

#masih dalam kondisi belum sempurna dan dapat dimodifikasi
collection = collections.BrokenBarHCollection.span_where(
       t, ymin=-1, ymax=0, where=s1<0, facecolor='white', alpha=1)
ax.add_collection(collection)
plt.show()
