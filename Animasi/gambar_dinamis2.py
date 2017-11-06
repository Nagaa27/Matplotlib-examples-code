# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

def f(x, y):
	return np.sin(x) + np.cos(y)

x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)

#ims adalah daftar dari setiap baris untuk digambarkan dalam frame
#disini kita hanya membuat animasi dari satu gambar dalam setiap frame
ims = []
for i in range(60):
	x += np.pi / 15
	y += np.pi / 20
	im = plt.imshow(f(x, y))
	ims.append([im])
	
ani = animation.ArtistAnimation(fig, ims, interval = 50, blit=True, 
	repeat_delay=1000)
plt.show()
