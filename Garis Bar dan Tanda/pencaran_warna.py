# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

import matplotlib.pyplot as plt
from numpy.random import rand

#membuat gabungan warna dengan 3 campuran warna dalam tampilan
for color in ['red', 'green', 'blue']:
	n = 750
	x, y = rand(2, n)
	scale = 200.0 * rand(n)
	plt.scatter(x, y, c=color, s=scale, label=color, alpha=0.3, 
						edgecolors='none')
plt.legend()
plt.grid(True)
plt.show()
