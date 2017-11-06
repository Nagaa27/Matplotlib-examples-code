# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

from matplotlib import pyplot
import matplotlib as mpl

#membuat sebuah gambar dan sumbu dengan dimensi yang diinginkan
fig = pyplot.figure(figsize=(8,3))
ax1 = fig.add_axes([0.05, 0.80, 0.9, 0.15])
ax2 = fig.add_axes([0.05, 0.475, 0.9, 0.15])
ax3 = fig.add_axes([0.05, 0.15, 0.9, 0.15])

#membuat peta warna dan aturan untuk mengikuti bagaimana data akan 
#dipilih dengan barwarna yang akan digunakan
cmap = mpl.cm.cool
norm = mpl.colors.Normalize(vmin=5, vmax=10)

#dasarwarnabar diarahkan dari ScalarMappable dan memasukkan sebuah 
#barwarna dalam sebuah sumbu yang spesifik, maka hal ini akan memiliki 
#seluruh yang dibutuhkan pada barwarna yang berdiri sendiri. 
#Ada lebih banyak kwargs, namun berikut adalah beberapa dasar barwarna
#yang berlanjut dengan ketebalan dan label
cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap,
                                   norm=norm,
                                   orientation='horizontal')
cb1.set_label('beberapa unit')

#contoh kedua yang diilustrasikan menggunakan sebuah ListedColormap, 
#sebuah BoundaryNorm, dan memperluas di akhir untuk menampilkan lebih 
#banyak/"over" dan "under" nilai warna
cmap = mpl.colors.ListedColormap(['r','g','b','c'])
cmap.set_over('0.25')
cmap.set_under('0.75')

#jika sebuah ListedColormap sudah digunakan, panjang dari ikatan array 
#harus lebih besar dari panjang daftar warna. Ikatan warna harus menaik 
#secara monoton
bounds = [1,2,4,7,8]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
cb2 = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm,
#untuk memperluas anda harus spesifik mengikat keduanya
boundaries=[0]+bounds+[13], extend='both', ticks=bounds, #dapat dipilih
spacing='proportional', orientation='horizontal')
cb2.set_label('Memiliki ciri interval, beberapa unit lainnya')

#contoh ketiga diilustrasikan menggunakan panjang yang sudah ditentukan 
#ekstensinya, menggunakan sebuah barwarna dengan ciri interval
cmap = mpl.colors.ListedColormap([[0., .4, 1.], [0., .8, 1.],
    [1., .8, 0.], [1., .4, 0.]])
cmap.set_over((1., 0., 0.))
cmap.set_under((0., 0., 1.))

bounds = [-1., -.5, 0., .5, 1.]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
cb3 = mpl.colorbar.ColorbarBase(ax3, cmap=cmap,
                                     norm=norm,
                                     boundaries=[-10]+bounds+[10],
                                     extend='both',
                                     #menentukan panjang pada tiap ekstensi
                                     #sama halnya dengan panjang
                                     #warna interior
                                     extendfrac='auto',
                                     ticks=bounds,
                                     spacing='uniform',
                                     orientation='horizontal')
cb3.set_label('Menentukan ekstensi panjang, beberapa unit lainnya')

pyplot.show()
