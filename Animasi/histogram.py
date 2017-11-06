# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path 
import matplotlib.animation as animation

fig, ax = plt.subplots()

#membuat data histogram dengan numpy
data = np.random.randn(1000)
n, bins = np.histogram(data, 100)

#menentukan sudut segiempat pada histogram
left = np.array(bins[:-1])
right = np.array (bins[1:])
bottom = np.zeros(len(left))
top = bottom + n
nrects = len(left)

#bagian menariknya adalah kita harus menentukan puncak dan path kode
#dengan menggunakan MOVEO, LINETO dan CLOSEPOLY
#pada bar terdapat : 1 pada MOVETO, 3 pada LINETO, 1 pada CLOSEPOLY
#penyangga closepoly diabaikan nmaun tetap dibutuhkan 
#agar kode tetap dibariskan secara vertikal
nverts = nrects*(1+3+1)
verts = np.zeros((nverts, 2))
codes = np.ones(nverts, int) * path.Path.LINETO
codes[0::5] = path.Path.MOVETO
codes[4::5] = path.Path.CLOSEPOLY
verts[0::5,0] = left
verts[0::5,1] = bottom
verts[1::5,0] = left
verts[1::5,1] = top
verts[2::5,0] = right
verts[2::5,1] = top
verts[3::5,0] = right
verts[3::5,1] = bottom

barpath = path.Path(verts, codes)
patch = patches.PathPatch(barpath, facecolor='green', edgecolor='yellow', alpha=0.5)
ax.add_patch(patch)

ax.set_xlim(left[0], right[-1])
ax.set_ylim(bottom.min(), top.max())

def animate(i):
	#simulasikan data yang sudah dimasukkan
	data = np.random.randn(1000)
	n, bins = np.histogram(data, 100)
	top = bottom = n
	verts[1::5,1] = top
	verts[2::5,1] = top
	
ani = animation.FuncAnimation(fig, animate, 100, repeat=False)
plt.show()
