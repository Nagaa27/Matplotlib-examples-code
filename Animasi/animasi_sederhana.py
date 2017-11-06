# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
#menentukan x-array
x = np.arange(0, 2*np.pi, 0.01)        
line, = ax.plot(x, np.sin(x))

#update data
def animate(i):
	line.set_ydata(np.sin(x+i/10.0)) 
	return line,
	
#init memberikan layar dilalui menjadi bersih
def init():
	line.set_ydata(np.ma.array(x, mask=True))
	return line,
	
ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
	interval = 25, blit=True)
plt.show()
