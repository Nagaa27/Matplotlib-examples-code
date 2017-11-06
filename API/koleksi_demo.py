# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

'''
Mendemonstrasikan Linecollection, PolyCollection dan 
RegularPolyCollection dengan skala otomatis.
Pada awal dua sub plot, kita akan menggunakan spiral.
Ukurannya akan ditentukan dalam plot unit, bukan unit data.
Posisinya akan ditentukan dalam data unit dengan menggunakan
"offsets" dan "transOffset" kwargs dari LineCollection dan PolyCollection.
Subplot ketiga akan membuat polygons digunakan secara umum,
dengan tipe yang sama pada skala dan posisi sebagaimana pada dua pertama.
Subplot yang terakhir akan diilustrasikan menggunakan "offsets=(xo,yo)",
karena sebuah tuple alternatif dalam daftar tuple, untuk menghasilkan 
kurva offset yang sukses, dengan offset yang dimasukkan dalam unit data.
Tindakan ini hanya terdapat pada linecollection.
'''


import matplotlib.pyplot as plt
from matplotlib import collections, transforms
from matplotlib.colors import colorConverter
import numpy as np

nverts = 50
npts = 100

#membuat beberapa spiral
r = np.array(range(nverts))
theta = np.array(range(nverts)) * (2*np.pi)/(nverts-1)
xx = r * np.sin(theta)
yy = r * np.cos(theta)
spiral = list(zip(xx,yy))

#membuat beberapa offsets
rs = np.random.RandomState([1234567])
xo = rs.randn(npts)
yo = rs.randn(npts)
xyo = list(zip(xo, yo))

#membuat sebuah daftar pada warna bersiklus melalui seri rgbcmyk 
colors = [colorConverter.to_rgba(c) for c in ('r','g','b','c','y','m','k')]
fig, axes = plt.subplots(2,2)
((ax1, ax2), (ax3, ax4)) = axes #membuka paket dari sumbu
			
col = collections.LineCollection([spiral], offsets=xyo,
                                transOffset=ax1.transData)
trans = fig.dpi_scale_trans + transforms.Affine2D().scale(1.0/72.0)
col.set_transform(trans) #titik pada pengubahan pixel

#catat : diawal argument pada pengenalan collection harus ada daftar 
#pada rangkaian pada x,y tuple : kita hanya memiliki satu rangkaian, 
#namun kita tetap harus memasukkannya ke dalam daftar
ax1.add_collection(col, autolim=True)

#autolim = True untuk mengaktifkan skala otomatis. 
#Pada cllection dengan offset seperti hal ini, hal ini memang 
#tidak efektif tidak juga akurat, namun hal ini cukup bagus untuk 
#menghasilkan sebuah plot dimana anda dapat menggunakkan sebagai 
#titik permulaan. Jika anda tahu sebelumnya  jarak dari x dan y 
#yang ingin anda tampilkan, hal ini lebih baik untuk menentukannya 
#secara eksplisit, hasil dari autolim kwarg (atau di tentukan menjadi False)
# dan menghilangkan 'ax1.autoscale_view()' dipanggil kebawah
#membuat sebuah transformasi pada segmen baris 
#seperti ukuran yang diberikan dalam posisi
col.set_color(colors)
ax1.autoscale_view()	#lihat komentar sebelumnya, setelah ax1.add_collection
ax1.set_title('LineCollection menggunakan offsets')
#data yang sama seperti sebelumnya, namun kurva diisi
col = collections.PolyCollection([spiral], offsets=xyo, transOffset=ax2.transData)
trans = transforms.Affine2D().scale(fig.dpi/72.0)
col.set_transform(trans)	#nilai diubahkan pada perubahan pixel
ax2.add_collection(col, autolim=True)
col.set_color(colors)
ax2.autoscale_view()
ax2.set_title('PolyCollection menggunakan offsets')

#7-sisi regular polygons
col = collections.RegularPolyCollection(7, sizes = np.fabs(xx)*10.0,
offsets=xyo, transOffset=ax3.transData)
trans = transforms.Affine2D().scale(fig.dpi/72.0)
col.set_transform(trans) #nilai diubahkan pada perubahan pixel
ax3.add_collection(col, autolim=True)
col.set_color(colors)
ax3.autoscale_view()
ax3.set_title('regularPolyCollection menggunakan offsets')

#simulasikan sebuah seri dari ocean pada profil saat ini,
#kesuksesan Offset dengan 0.1 m/s maka bentuknya adalah apa yang disebut
#dengan plot "air terjun" atau plot "goyangan"
nverts = 60
ncurves = 20
offs = (0.1, 0.0)

yy = np.linspace(0, 2*np.pi, nverts)
ym = np.amax(yy)
xx = (0.2 + (ym-yy)/ym)**2 * np.cos(yy-0.4) * 0.5
segs = []
for i in range(ncurves):
	xxx = xx + 0.02*rs.randn(nverts)
	curve = list(zip(xxx, yy*100))
	segs.append(curve)
	
col = collections.LineCollection(segs, offsets=offs)
ax4.add_collection(col, autolim=True)
col.set_color(colors)
ax4.autoscale_view()
ax4.set_title('Data offsets berhasil')
ax4.set_xlabel('Kecepatan komponen daerah (m/s)')
ax4.set_ylabel('Kedalaman (m)')
#membalikkan sudut-y semakin dalam kedalam
ax4.set_ylim(ax4.get_ylim()[::-1])

plt.show()
