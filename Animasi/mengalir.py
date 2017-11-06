# Matius Celcius Sinaga
# Credit : Nicolas P. Rougier
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#membuat gambar baru dengan latar gelap
fig = plt.figure(figsize=(8, 8), facecolor='black')

#menambahkan sebuah subplot dengan tanpa frame
ax = plt.subplot(111, frameon=False)

#menghasilkan data acak
data = np.random.uniform(0, 1, (64, 75))
X = np.linspace(-1, 1, data.shape[-1])
G = 1.5 * np.exp(-4 * X * X)

#menghasilkan baris plot
lines = []
for i in range(len(data)):
	#penguraian kecil pada perluasan  X untuk mendapatkan
	#efek perspektive yang rendah
	xscale =1 - i / 200
	#sama dengan linewidth (tekanan di bawah)
	lw = 1.5 - i / 100.0
	line, = ax.plot(xscale * X, i + G * data[i], color="w", lw=lw)
	lines.append(line)
	
#menentukan batas y atau baris awal yang dipotong karana ketebalannya
ax.set_ylim(-1, 70)

#tanpa ketebalan
ax.set_xticks([])
ax.set_yticks([])

#dua bagian judul untuk mendapatkan perbedaan ukuran font
ax.text(0.5, 1.0, "MATPLOTLIB", transform=ax.transAxes, ha="right", 
		va="bottom", color="w", family="sans-serif", fontweight="light",
		fontsize=16)
ax.text(0.5, 1.0, "'NAGA", transform=ax.transAxes, ha="left", 
		va="bottom", color="w", family="sans-serif", fontweight="light",
		fontsize=16)		
#update fungsi
def update(*args):
	#menggeser seluruh data ke kanan
	data[:, 1:] = data[:, :-1]
	
	#mengisi dengan nilai baru
	data[:, 0] = np.random.uniform(0, 1, len(data))
	
	#update data
	for i in range(len(data)):
		lines[i].set_ydata(i + G * data[i])
		
	#menghasilkan modifikasi
	return lines

#membangun animasi, menggunakan update fungsi sebagai pengarah animasi
anim = animation.FuncAnimation(fig, update, interval=10)
plt.show()
	
