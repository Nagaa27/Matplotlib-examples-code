# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

"""
Pada contoh ini menggunakan 'circle' atau 'polygon', kerangka polygon
tidak memiliki gridline (garis lingkaran sebagai pengganti polygon).
Hal ini dimungkinkan bila polygon menentukan GRIDLINE_INTERPOLATION_STEPS
dalam matplotlib.axis yang dibutuhkan pada vertices, namun berorientasi 
pada polygon dan tidak pada sumbu radial
http://en.wikipedia.org/wiki/Radar_chart
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection


def radar_factory(num_vars, frame='circle'):
    """Membuat radar grafik dengan `num_vars` 
    Fungsi ini akan membuat projek RadarAxes dan mengenalkannya

    Parameters
    ----------
    num_vars : int
        Number of variables for radar chart.
    frame : {'circle' | 'polygon'}
        Shape of frame surrounding axes.

    """
    #menghitung kedataran ruang dalam sudut sumbu
    theta = 2*np.pi * np.linspace(0, 1-1./num_vars, num_vars)
    #merotasi theta seperti pada sumbu paling atas 
    theta += np.pi/2

    def draw_poly_patch(self):
        verts = unit_poly_verts(theta)
        return plt.Polygon(verts, closed=True, edgecolor='k')

    def draw_circle_patch(self):
        #unit lingkaran pada pertengahan
        return plt.Circle((0.5, 0.5), 0.5)

    patch_dict = {'polygon': draw_poly_patch, 'circle': draw_circle_patch}
    if frame not in patch_dict:
        raise ValueError('nilai tidak diketahui pada `frame`: %s' % frame)

    class RadarAxes(PolarAxes):
        name = 'radar'
        #menggunakan satu baris segment untuk menghubungkan point spesifik
        RESOLUTION = 1
        #menjelaskan metode draw_frame
        draw_patch = patch_dict[frame]

        def fill(self, *args, **kwargs):
            #menghindari pengisian garis dengan cepat secara otomatis
            closed = kwargs.pop('closed', True)
            return super(RadarAxes, self).fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            #menghindari pengisian garis dengan cepat secara otomatis
            lines = super(RadarAxes, self).plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            # Tetapkan tanda pada x[0], y[0] dengan double
            if x[0] != x[-1]:
                x = np.concatenate((x, [x[0]]))
                y = np.concatenate((y, [y[0]]))
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(theta * 180/np.pi, labels)

        def _gen_axes_patch(self):
            return self.draw_patch()

        def _gen_axes_spines(self):
            if frame == 'circle':
                return PolarAxes._gen_axes_spines(self)
            # The following is a hack to get the spines (i.e. the axes frame)
            # to draw correctly for a polygon frame.

            # spine_type haruslah 'left', 'right', 'top', 'bottom', or `circle`.
            spine_type = 'circle'
            verts = unit_poly_verts(theta)
            # menghentikan sementara polygon dengan mengulangi vertex awal
            verts.append(verts[0])
            path = Path(verts)

            spine = Spine(self, spine_type, path)
            spine.set_transform(self.transAxes)
            return {'polar': spine}

    register_projection(RadarAxes)
    return theta


def unit_poly_verts(theta):
    """mengembalikan puncak(vertices) dari polyon dari sumbu subplot
	Polygon ini membatasi dengan sebuah unit lingkaran ditengah (0.5, 0.5)
	"""
    x0, y0, r = [0.5] * 3
    verts = [(r*np.cos(t) + x0, r*np.sin(t) + y0) for t in theta]
    return verts


def example_data():
    """
	data berikut berasal dari Denver Aerosol Sources and Health
	(doi:10.1016/j.atmosenv.2008.12.017)
	data ini adalah sumber polusi yang diestimasi dalam 5 model
	sumber seperti berasal dari mobil, pembakaran hutan dll yang menghasilkan
	7-8 bentuk bahan kimia. Pada layar yang sudah diuji ada beberapa 
	yang dapat kita lihat jika kita mampu memisualisasikan bagaimana 
	sumber model berubah melalui 4 skenario :
		1. Bukan gas yang dihasilkan secara khusus, hanya 7 bentuk khusus
				Sulfate
				Nitrate
				Elemental Carbon (EC)
				Organic Carbon fraction 1 (OC)
				Organic Carbon fraction 2 (OC2)
				Organic Carbon fraction 3 (OC3)
				Pyrolized Organic Carbon (OP)
		2. Dicantumkan pada bentuk gas dengan carbon monoksida (CO)
		3. Dicantumkan pada bentuk gas dengan ozone (O3)
		4. Dicantumkan pada bentuk gas dengan bentuk khusus
	"""
    data = {
        'column names':
            ['Sulfate', 'Nitrate', 'EC', 'OC1', 'OC2', 'OC3', 'OP', 'CO',
             'O3'],
        'Basecase':
            [[0.88, 0.01, 0.03, 0.03, 0.00, 0.06, 0.01, 0.00, 0.00],
             [0.07, 0.95, 0.04, 0.05, 0.00, 0.02, 0.01, 0.00, 0.00],
             [0.01, 0.02, 0.85, 0.19, 0.05, 0.10, 0.00, 0.00, 0.00],
             [0.02, 0.01, 0.07, 0.01, 0.21, 0.12, 0.98, 0.00, 0.00],
             [0.01, 0.01, 0.02, 0.71, 0.74, 0.70, 0.00, 0.00, 0.00]],
        'With CO':
            [[0.88, 0.02, 0.02, 0.02, 0.00, 0.05, 0.00, 0.05, 0.00],
             [0.08, 0.94, 0.04, 0.02, 0.00, 0.01, 0.12, 0.04, 0.00],
             [0.01, 0.01, 0.79, 0.10, 0.00, 0.05, 0.00, 0.31, 0.00],
             [0.00, 0.02, 0.03, 0.38, 0.31, 0.31, 0.00, 0.59, 0.00],
             [0.02, 0.02, 0.11, 0.47, 0.69, 0.58, 0.88, 0.00, 0.00]],
        'With O3':
            [[0.89, 0.01, 0.07, 0.00, 0.00, 0.05, 0.00, 0.00, 0.03],
             [0.07, 0.95, 0.05, 0.04, 0.00, 0.02, 0.12, 0.00, 0.00],
             [0.01, 0.02, 0.86, 0.27, 0.16, 0.19, 0.00, 0.00, 0.00],
             [0.01, 0.03, 0.00, 0.32, 0.29, 0.27, 0.00, 0.00, 0.95],
             [0.02, 0.00, 0.03, 0.37, 0.56, 0.47, 0.87, 0.00, 0.00]],
        'CO & O3':
            [[0.87, 0.01, 0.08, 0.00, 0.00, 0.04, 0.00, 0.00, 0.01],
             [0.09, 0.95, 0.02, 0.03, 0.00, 0.01, 0.13, 0.06, 0.00],
             [0.01, 0.02, 0.71, 0.24, 0.13, 0.16, 0.00, 0.50, 0.00],
             [0.01, 0.03, 0.00, 0.28, 0.24, 0.23, 0.00, 0.44, 0.88],
             [0.02, 0.00, 0.18, 0.45, 0.64, 0.55, 0.86, 0.00, 0.16]]}
    return data


if __name__ == '__main__':
    N = 9
    theta = radar_factory(N, frame='polygon')

    data = example_data()
    spoke_labels = data.pop('column names')

    fig = plt.figure(figsize=(9, 9))
    fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)

    colors = ['b', 'r', 'g', 'm', 'y']
    #alur dalam empat bentuk contoh data yang terpisah
    for n, title in enumerate(data.keys()):
        ax = fig.add_subplot(2, 2, n+1, projection='radar')
        plt.rgrids([0.2, 0.4, 0.6, 0.8])
        ax.set_title(title, weight='bold', size='medium', position=(0.5, 1.1),
                     horizontalalignment='center', verticalalignment='center')
        for d, color in zip(data[title], colors):
            ax.plot(theta, d, color=color)
            ax.fill(theta, d, facecolor=color, alpha=0.25)
        ax.set_varlabels(spoke_labels)

    #menambahkan karakter relatif pada kiri atas plot
    plt.subplot(2, 2, 1)
    labels = ('Faktor 1', 'Faktor 2', 'Faktor 3', 'Faktor 4', 'Faktor 5')
    legend = plt.legend(labels, loc=(0.9, .95), labelspacing=0.1)
    plt.setp(legend.get_texts(), fontsize='small')

    plt.figtext(0.5, 0.965, '5-Faktor Peyelesaian Dengan 4 Contoh Skenario',
                ha='center', color='black', weight='bold', size='large')
    plt.show()
