# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as p3
import matplotlib.animation as animation

def Gen_RandLine(length, dims=2) :
	"""
	Membuat sebuah baris menggunakan algoritma berjalan acak
	length adalah panjang pada jumlah baris poin
	dims adalah jumlah dimensi dari baris yang ada
	"""
	lineData = np.empty((dims, length))
	lineData[:, 0] = np.random.rand(dims)
	for index in range(1, length) :
		#skala dari angka acak adalah dari 1 dan selanjunya
		#pergerakan adalah perubahan kecil pada posisi
		#substraksi dengan 0.5 adalah untuk merubah jarakpada [-0.5, 0.5]
		#untuk mengijinkan sebuah garis bergerak kebelakang
		step = ((np.random.rand(dims) - 0.5) * 0.1)
		lineData[:, index] = lineData[:, index-1] + step
		
	return lineData
	
def update_lines(num, dataLines, lines) :
	for line, data in zip(lines, dataLines) :
		#catat tidak ada penomoran .set_data() pada 3 dim data
		line.set_data(data[0:2, :num])
		line.set_3d_properties(data[2, :num])
	return lines

#melampirkan sumbu 3D pada gambar
fig = plt.figure()
ax = p3.Axes3D(fig)

data = [Gen_RandLine(27, 3) for index in range(50)]

#membuat 50 baris objek
#catat : tidak dapat melewati array kosong dalam versi 3D pada plot()
lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]

#menentukan smbu properties
ax.set_xlim3d([0.0, 1.0])
ax.set_xlabel('X')

ax.set_ylim3d([0.0, 1.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 1.0])
ax.set_zlabel('Z')

ax.set_title('3D Test ')

#membuat objek animasi
line_ani = animation.FuncAnimation(fig, update_lines, 27, fargs=(data, lines), interval=50, blit=False)
plt.show()

