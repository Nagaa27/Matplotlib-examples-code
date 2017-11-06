# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

#update distribusi berdasarkan data baru
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
from matplotlib.animation import FuncAnimation

class UpdateDist(object):
    def __init__(self, ax, prob=0.5):
        self.success = 0
        self.prob = prob
        self.line, = ax.plot([], [], 'k-')
        self.x = np.linspace(0, 1, 200)
        self.ax = ax

        #menentukan parameter plot
        self.ax.set_xlim(0, 1)
        #10 adalah nilai yang anda tentukan
        self.ax.set_ylim(0, 10)
        self.ax.grid(True)

        #garis vertikal menghadirkan nilai teoritikal
		#yang dimana mendistribusikan plotnya haruslah korvergen
		#menuju satu titik
		#color adalah warna garis tengah
        self.ax.axvline(prob, linestyle='--', color='green')

    def init(self):
        self.success = 0
        self.line.set_data([], [])
        return self.line,

    def __call__(self, i):
        #plot ini akan berjalan terus menerus dan 
			#kita akan melihat hubungan yang baru baru
        if i == 0:
            return self.init()

        #pilih dasar keberhasilan melebihi batas dengan membuat keseragaman
        if np.random.rand(1,) < self.prob:
            self.success += 1
        y = ss.beta.pdf(self.x, self.success + 1, (i - self.success) + 1)
        self.line.set_data(self.x, y)
        return self.line,

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ud = UpdateDist(ax, prob=0.7)
anim = FuncAnimation(fig, ud, frames=np.arange(100), init_func=ud.init,
        interval=100, blit=True)
plt.show()
