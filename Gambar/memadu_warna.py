# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

#menampilkan kombinasi Normalisasi dan Colormap dengan level pada pcolor
#pcolormesh dan imshow tipe plot yang sama dengan level argumen katakunci
#pada contour/contourf
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np

#membuat hal ini lebih kecil untuk kenaikan resolusi
dx, dy = 0.05, 0.05

#mengubah 2d pada batas x dan y
y, x = np.mgrid[slice(1, 5 + dy, dy), slice(1, 5 + dx, dx)]
z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

#x dan y dibatasi, maka z harus bernilai pada batasannya
#selanjutnya, mengubah nilai akhir dari array z
z = z[:-1, :-1]
levels = MaxNLocator(nbins=15).tick_values(z.min(), z.max())
#memilih colormap, level dan mendefinisikan normalization
#dengan memilih nilai data dan menerjemahkannya dalam level
cmap = plt.get_cmap('PiYG')
norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

plt.subplot(2, 1, 1)
im = plt.pcolormesh(x, y, z, cmap=cmap, norm=norm)
plt.colorbar()
#menentukan batasan pada plot dengan batas pada data
plt.axis([x.min(), x.max(), y.min(), y.max()])
plt.title('pcolormesh dengan levels')



plt.subplot(2, 1, 2)
#contours adalah nilai dasar, maka diubah menjadi nilai tengah
plt.contourf(x[:-1, :-1] + dx / 2.,
             y[:-1, :-1] + dy / 2., z, levels=levels,
             cmap=cmap)
plt.colorbar()
plt.title('contourf dengan levels')


plt.show()
