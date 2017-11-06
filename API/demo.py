# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

import numpy as np
import matplotlib.pyplot as plt

#membuat data palse
a = b = np.arange(0,3, .02)
c = np.exp(a)
d = c[::-1]

#membuat plot dengan menjelaskan label sebelumnya
plt.plot(a, c, 'k--', label='Panjang Model ')
plt.plot(a, d, 'k:', label='Panjang Data ')
plt.plot(a, c+d, 'k', label='Total panjang pesan ')

legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')
#memasukkan latar belakang warna
legend.get_frame().set_facecolor('#00FFCC')
plt.show()
