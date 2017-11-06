# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_line(num, data, line):
	line.set_data(data[...,:num])
	return line,
	
fig1 = plt.figure()

data = np.random.rand(2, 25)
l, = plt.plot([], [], 'r-')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x')

#jika ingin mengubah judul disini
plt.title('Garis-garis Abstrak')
line_ani = animation.FuncAnimation(fig1, update_line, 25, fargs=(data, l), interval=50, blit=True)
#line_ani tersimpan sebagai('lines.mp4')

fig2 = plt.figure()

x = np.arange(-9,10)
y = np.arange(-9, 10).reshape(-1, 1)
base = np.hypot(x, y)
ims = []
for add in np.arange(15):
	ims.append((plt.pcolor(x, y, base + add, norm=plt.Normalize(0, 30)),))
	
im_ani = animation.ArtistAnimation(fig2, ims, interval=50, repeat_delay=3000, blit=True)
#im_ani.tersimpan sebagai (im.mp4', metadata={'artist':'Matius Celcius Sinaga'})

#ubah judul disini
plt.title('Transisi warna')

plt.show()
