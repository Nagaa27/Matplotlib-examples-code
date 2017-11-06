# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

#data acak menggunakan random.randn
x = np.random.randn(1000)
y = np.random.randn(1000)

fig, axScatter = plt.subplots(figsize=(5.5,5.5))

#pembagian dilakukan disini pada plot
axScatter.scatter(x, y)
axScatter.set_aspect(1.)

#membuat sumbu baru pada kanan dan atas sumbu . Argumen awal pada new_vertical
#atau new_horizontal metodenya pada tinggi dan lebar pada sumbu yang dibuat
#dalam satuan inci
divider = make_axes_locatable(axScatter)
axHistx = divider.append_axes("top", 1.2, pad=0.1, sharex=axScatter)
axHisty = divider.append_axes("right", 1.2, pad=0.1, sharey=axScatter)

#membuat beberapa label tidak dapat terlihat
plt.setp(axHistx.get_xticklabels() + axHisty.get_yticklabels(),
			visible=False)

#menentukan batasan diawal			
binwidth = 0.25
xymax = np.max([np.max(np.fabs(x)), np.max(np.fabs(y))])
lim = (int(xymax/binwidth) + 1) * binwidth

bins = np.arange(-lim, lim + binwidth, binwidth)
axHistx.hist(x, bins=bins)
axHisty.hist(y, bins=bins, orientation='horizontal')

#xaxis dari axHistx dan yaxis dari axHist dibagi dengan axScatter, maka 
#tidak ada yang ditentukan dengan cara manual pada xlim dan ylim pada sumbu
for tl in axHistx.get_xticklabels():
	tl.set_visible(False)
axHistx.set_yticks([0, 50, 100])

for tl in axHisty.get_yticklabels():
	tl.set_visible(False)
axHistx.set_xticks([0, 50, 100])

plt.draw()
plt.show()
