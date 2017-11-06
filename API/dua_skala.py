# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

"""
Mendemonstrasikan bagaimana dua alur pada sumbu yang sama dengan skala kiri-kanan
Sumbu segiempat kerangkanya berhenti pada sumbu ke dua dan mnejaganya tetap diawal
Anda dapat menggunakan pembagian matplotlib.ticker formatter dan locators sebagai
kelengkapan karena kedua sumbu tersendiri
Metode twinx dan twiny dijelaskan sebagai fungsi pyplot
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
t = np.arange(0.01, 10.0, 0.01)
s1 = np.exp(t)
ax1.plot(t, s1, 'b-')
ax1.set_xlabel('time(s)')

ax1.set_ylabel('exp', color='b')
for tl in ax1.get_yticklabels():
	tl.set_color('b')
	
ax2 = ax1.twinx()
s2 = np.sin(2*np.pi*t)
ax2.plot(t, s2, 'r.')
ax2.set_ylabel('sin', color='r')
for tl in ax2.get_yticklabels():
	tl.set_color('r')
plt.show()
