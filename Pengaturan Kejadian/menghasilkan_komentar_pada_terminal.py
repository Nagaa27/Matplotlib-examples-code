# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

from __future__ import print_function
import matplotlib.pyplot as plt

def handle_close(evt):
	print('Tutup tampilan menghasilkan komentar pada terminal')
fig = plt.figure()
fig.canvas.mpl_connect('close_event', handle_close)
plt.text(0.02, 0.5, 'Tutup tampilan menghasilkan komentar pada terminal',
		dict(size=15))
plt.show()
