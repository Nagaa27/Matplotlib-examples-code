# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

#membuat dua panel indikator. Perbesaran pada panel kanan akan menghasilkan
#segiempat pada panel pertama dan  penanda daerah pada panel kedua.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

#subkelas segiempat akan dipanngil dalam contoh sumbu, menghasilkan segiempat
#yang berbentuk sesuai dengan batasan pada sumbu
class UpdatingRect(Rectangle):
    def __call__(self, ax):
        self.set_bounds(*ax.viewLim.bounds)
        ax.figure.canvas.draw_idle()

#sebuah kelas akan menghasilkan pola sesuai dengan masukan,
#maka anda harus memperhatikan kenaikan secara detail
#dalam box dikiri panel akan dihasilkan area yang telah diperbesar
class MandlebrotDisplay(object):
    def __init__(self, h=500, w=500, niter=50, radius=2., power=2):
        self.height = h
        self.width = w
        self.niter = niter
        self.radius = radius
        self.power = power

    def __call__(self, xstart, xend, ystart, yend):
        self.x = np.linspace(xstart, xend, self.width)
        self.y = np.linspace(ystart, yend, self.height).reshape(-1,1)
        c = self.x + 1.0j * self.y
        threshold_time = np.zeros((self.height, self.width))
        z = np.zeros(threshold_time.shape, dtype=np.complex)
        mask = np.ones(threshold_time.shape, dtype=np.bool)
        for i in range(self.niter):
            z[mask] = z[mask]**self.power + c[mask]
            mask = (np.abs(z) < self.radius)
            threshold_time += mask
        return threshold_time

    def ax_update(self, ax):
        ax.set_autoscale_on(False) #jika sebaliknya melakukan perulangan tiada akhir

        #menampilkan jumlah point dari jumlah pixel pada jendela
        dims = ax.axesPatch.get_window_extent().bounds
        self.width = int(dims[2] + 0.5)
        self.height = int(dims[2] + 0.5)

        #menentukan rentang pada area baru
        xstart,ystart,xdelta,ydelta = ax.viewLim.bounds
        xend = xstart + xdelta
        yend = ystart + ydelta

        #mengupdate objek gambar dengan data baru dan perluasannya
        im = ax.images[-1]
        im.set_data(self.__call__(xstart, xend, ystart, yend))
        im.set_extent((xstart, xend, ystart, yend))
        ax.figure.canvas.draw_idle()

md = MandlebrotDisplay()
Z = md(-2., 0.5, -1.25, 1.25)

fig1, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(Z, origin='lower', extent=(md.x.min(), md.x.max(), md.y.min(), md.y.max()))
ax2.imshow(Z, origin='lower', extent=(md.x.min(), md.x.max(), md.y.min(), md.y.max()))

rect = UpdatingRect([0, 0], 0, 0, facecolor='None', edgecolor='black')
rect.set_bounds(*ax2.viewLim.bounds)
ax1.add_patch(rect)

#menghubungkan pada perubahan batasan pandangan
ax2.callbacks.connect('xlim_changed', rect)
ax2.callbacks.connect('ylim_changed', rect)

ax2.callbacks.connect('xlim_changed', md.ax_update)
ax2.callbacks.connect('ylim_changed', md.ax_update)

plt.show()
