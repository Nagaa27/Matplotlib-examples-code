# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

#menggunakan waktu terbaru untuk dijadikan judul dalam tampilan
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def update_title(axes):
	axes.set_title(datetime.now())
	axes.figure.canvas.draw()
fig, ax = plt.subplots()
x = np.linspace(-3,3)
ax.plot(x, x*x)

#membuat objek waktu terbaru
#menentukan interval 500 milliseconds
timer = fig.canvas.new_timer(interval=100)
timer.add_callback(update_title, ax)
timer.start()

plt.show()
