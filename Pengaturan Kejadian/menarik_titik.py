# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

"""
Menampilkan aplikasi GUI dengan menggunakan matplotlib dengan mengatur 
interaksi pada objek di layar
"""
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.artist import Artist
from matplotlib.mlab import dist_point_to_segment


class PolygonInteractor:
    """
    Pengaturan PolygonInteractor

    Kumpulan kunci:

      't' titik dengan tanda on and off. jika tanda on maka anda dapat 
		  merubah bahkan menghapusnya

      'd' menghapus titik paling bawah

      'i' memasukkan nilai teratas. Dalam epsilon pada penghubung dua titik puncak
    """

    showverts = True
    epsilon = 5  #pixel terbesar penghubung nilai terbanyak

    def __init__(self, ax, poly):
        if poly.figure is None:
            raise RuntimeError('Anda harus menambahkan polygon diawal untuk menggambarkan atau menjelaskan interaksi')
        self.ax = ax
        canvas = poly.figure.canvas
        self.poly = poly

        x, y = zip(*self.poly.xy)
        self.line = Line2D(x, y, marker='o', markerfacecolor='r', animated=True)
        self.ax.add_line(self.line)
        #self._update_line(poly)

        cid = self.poly.add_callback(self.poly_changed)
        self._ind = None #mengaktifkan vert

        canvas.mpl_connect('draw_event', self.draw_callback)
        canvas.mpl_connect('button_press_event', self.button_press_callback)
        canvas.mpl_connect('key_press_event', self.key_press_callback)
        canvas.mpl_connect('button_release_event', self.button_release_callback)
        canvas.mpl_connect('motion_notify_event', self.motion_notify_callback)
        self.canvas = canvas


    def draw_callback(self, event):
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        self.ax.draw_artist(self.poly)
        self.ax.draw_artist(self.line)
        self.canvas.blit(self.ax.bbox)

    def poly_changed(self, poly):
        'metode ini akan dipanggil ketika objek polygon sudah dipanggil'
        #hanya salinan hasil pada garis (kecuali bentuk nyata)
        vis = self.line.get_visible()
        Artist.update_from(self.line, poly)
        self.line.set_visible(vis)  #jangan menggunakan daerah pola yang nyata
		

    def get_ind_under_point(self, event):
        'menentukan index dari titik terbawah dengan toleransi'
        #menampilkan koordinat
        xy = np.asarray(self.poly.xy)
        xyt = self.poly.get_transform().transform(xy)
        xt, yt = xyt[:, 0], xyt[:, 1]
        d = np.sqrt((xt-event.x)**2 + (yt-event.y)**2)
        indseq = np.nonzero(np.equal(d, np.amin(d)))[0]
        ind = indseq[0]

        if d[ind]>=self.epsilon:
            ind = None

        return ind

    def button_press_callback(self, event):
        'ketika tombol mouse sudah ditekan'
        if not self.showverts: return
        if event.inaxes==None: return
        if event.button != 1: return
        self._ind = self.get_ind_under_point(event)

    def button_release_callback(self, event):
        'ketika tombol mouse sudah dilepas'
        if not self.showverts: return
        if event.button != 1: return
        self._ind = None

    def key_press_callback(self, event):
        'ketika kunci sudah ditekan '
        if not event.inaxes: return
        if event.key=='t':
            self.showverts = not self.showverts
            self.line.set_visible(self.showverts)
            if not self.showverts: self._ind = None
        elif event.key=='d':
            ind = self.get_ind_under_point(event)
            if ind is not None:
                self.poly.xy = [tup for i,tup in enumerate(self.poly.xy) if i!=ind]
                self.line.set_data(zip(*self.poly.xy))
        elif event.key=='i':
            xys = self.poly.get_transform().transform(self.poly.xy)
            p = event.x, event.y # display coords
            for i in range(len(xys)-1):
                s0 = xys[i]
                s1 = xys[i+1]
                d = dist_point_to_segment(p, s0, s1)
                if d<=self.epsilon:
                    self.poly.xy = np.array(
                        list(self.poly.xy[:i]) +
                        [(event.xdata, event.ydata)] +
                        list(self.poly.xy[i:]))
                    self.line.set_data(zip(*self.poly.xy))
                    break


        self.canvas.draw()

    def motion_notify_callback(self, event):
        'mouse dalam pergerakan'
        if not self.showverts: return
        if self._ind is None: return
        if event.inaxes is None: return
        if event.button != 1: return
        x,y = event.xdata, event.ydata

        self.poly.xy[self._ind] = x,y
        self.line.set_data(zip(*self.poly.xy))

        self.canvas.restore_region(self.background)
        self.ax.draw_artist(self.poly)
        self.ax.draw_artist(self.line)
        self.canvas.blit(self.ax.bbox)


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon

    theta = np.arange(0, 2*np.pi, 0.1)
    r = 1.5

    xs = r*np.cos(theta)
    ys = r*np.sin(theta)

    poly = Polygon(list(zip(xs, ys)), animated=True)

    fig, ax = plt.subplots()
    ax.add_patch(poly)
    p = PolygonInteractor(ax, poly)

    #ax.add_line(p.line)
    ax.set_title('Klik dan drag titik untuk merubahnya')
    ax.set_xlim((-2,2))
    ax.set_ylim((-2,2))
    plt.show()

