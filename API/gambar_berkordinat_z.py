# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

"""
Menampilkan bagaimana cara memodifikasi format kordinat pada pelaporan 
gambar "z" nilai dari pixel terdekat yang diberikan pada x dan y
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

X = 10*np.random.rand(5,3)

fig, ax = plt.subplots()
ax.imshow(X, cmap=cm.jet, interpolation='nearest')

numrows, numcols = X.shape
def format_coord(x, y):
    col = int(x+0.5)
    row = int(y+0.5)
    if col>=0 and col<numcols and row>=0 and row<numrows:
        z = X[row,col]
        return 'x=%1.4f, y=%1.4f, z=%1.4f'%(x, y, z)
    else:
        return 'x=%1.4f, y=%1.4f'%(x, y)

ax.format_coord = format_coord
plt.show()

