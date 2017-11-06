# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

"""
Contoh ini menunjukkan bagaimana menggunakan penambalan path untuk 
menggambarkan beberapa segiempat. Teknik ini menggunakan contoh segiempat, 
atau metode yang cepat menggunakan PolyCollection, dimana 
mengimplementasikan sebelum kita memiliki path yang cocok dengan 
moveto/lineto, closepoly kecuali in mpl. Sekarang kita harus melakukannya, 
kita dapat menggambarkan collections pada bentuk objek yang umum dengan 
properties homogeus lebih efisien dengan PathCollection. contoh ini 
membuat histogram lebih baik dalam bekerja menentukan array vertex sebagai 
keluaran, namun hal ini lebih cepat pada jumlah yang lebih luas pada objek
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

fig, ax = plt.subplots()

#data histogram dengan numpy
data = np.random.randn(1000)
n, bins = np.histogram(data, 50)

#menentukan sudut dari segiempat pada histogram
left = np.array(bins[:-1])
right = np.array(bins[1:])
bottom = np.zeros(len(left))
top = bottom + n

#kita membutuhkan (numrects x numsides x 2) array numpy pada path bantuan
#fungsi untuk membentuk komponen path
XY = np.array([[left, left, right,right], [bottom,top,top,bottom]]).T

#menentukan objek path
barpath = path.Path.make_compound_path_from_polys(XY)

#membuat patch keluaran
patch = patches.PathPatch(barpath, facecolor='blue', edgecolor='gray',
alpha=0.8)
ax.add_patch(patch)

#mengapdate batas kunjungan
ax.set_xlim(left[0], right[-1])
ax.set_ylim(bottom.min(), top.max())

plt.show()
