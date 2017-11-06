# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

"""
Mirip dengan Osiloskop. Membutuhkan animasi API dalam matplotlib 1.0 SVN
"""

import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Scope:
    def __init__(self, ax, maxt=2, dt=0.02):
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-.1, 1.1)
        self.ax.set_xlim(0, self.maxt)

    def update(self, y):
        lastt = self.tdata[-1]
        if lastt > self.tdata[0] + self.maxt: #mereset array
            self.tdata = [self.tdata[-1]]
            self.ydata = [self.ydata[-1]]
            self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
            self.ax.figure.canvas.draw()

        t = self.tdata[-1] + self.dt
        self.tdata.append(t)
        self.ydata.append(y)
        self.line.set_data(self.tdata, self.ydata)
        return self.line,
		
def emitter(p=0.03):
	'menghasilkan sebuah nilai acak dengan kemungkinan p, lainnya 0'
	while True:
		v = np.random.rand(1)
		if v > p:
			yield 0
		else:
			yield np.random.rand(1)

fig, ax = plt.subplots()
scope = Scope(ax)

#melewati sebuah generator "emitter" untuk menghasilkan data pada update func
ani = animation.FuncAnimation(fig, scope.update, emitter, interval=10, blit=True)

plt.show()
