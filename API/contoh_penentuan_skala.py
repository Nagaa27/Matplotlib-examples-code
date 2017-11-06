# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

from __future__ import unicode_literals
import numpy as np
from numpy import ma
from matplotlib import scale as mscale
from matplotlib import transforms as mtransforms
from matplotlib.ticker import Formatter, FixedLocator


class MercatorLatitudeScale(mscale.ScaleBase):
    """
    Data skala dalam rentang -pi/2 ke pi/2 (-90 pada 90 derajat)menggunakan
    sistem pada skala latitude
    
    The scale function:
      ln(tan(y) + sec(y))

    The inverse scale function:
      atan(sinh(y))
    sumber:
    http://en.wikipedia.org/wiki/Mercator_projection
    """

    #kelas sekala harus memiliki anggota ``name`` yang mendefinisikan
    #string yang digunakan untuk memilih skala ``gca().set_yscale("mercator")`` 
    #yang digunakan nantinya
    name = 'mercator'

    def __init__(self, axis, **kwargs):
        #Setiap argumen kata kunci yang melalui ``set_xscale`` dan
        #``set_yscale`` juga akan melewati konstruktor skala
        #derajat sebelumnya dipilih melalui crop data
        mscale.ScaleBase.__init__(self)
        thresh = kwargs.pop("thresh", (85 / 180.0) * np.pi)
        if thresh >= np.pi / 2.0:
            raise ValueError("thresh kurang dari pi/2")
        self.thresh = thresh

    def get_transform(self):
        #kelas MercatorLatitudeTransform didefiniskan sebagai berikut
        return self.MercatorLatitudeTransform(self.thresh)

    def set_default_locators_and_formatters(self, axis):
        #jika hanya skala membutuhkan kostum locator dan formatter
        #menlis kostum dan locator dan formatter lebih kearah diluar lingkup
        #contoh kali ini. Dalam hal ini, contoh Mercator digunakan sebagai
        #locator -90 sampai 90 derajat dan kostum kelas formatter untuk
        #mengubah radian menjadi derajat dan memasukkan simbol derajat
        #seteleh nilai
        class DegreeFormatter(Formatter):
            def __call__(self, x, pos=None):
                # \u00b0 : simbol derajat
                return "%d\u00b0" % ((x / np.pi) * 180.0)

        deg2rad = np.pi / 180.0
        axis.set_major_locator(FixedLocator(
                np.arange(-90, 90, 10) * deg2rad))
        axis.set_major_formatter(DegreeFormatter())
        axis.set_minor_formatter(DegreeFormatter())

    def limit_range_for_scale(self, vmin, vmax, minpos):
        return max(vmin, -self.thresh), min(vmax, self.thresh)

    class MercatorLatitudeTransform(mtransforms.Transform):
        #ada dua anggota nilai yang harus didefinisikan ``input_dims`` 
        #dan ``output_dims`` jumlah spesifik pada dimensi masukan dan keluaran
        #pada transformasi. Hal ini digunakan pada framework transformasi
        #untuk melakukan beberapa error checking dan pencegahan transformasi
        #yang tidak cocok pada saat menyambungkan. Ketika menjelaskan transformasi
        #pada sebuah skala, dengan penjelasan, dipisah dan hanya memiliki
        #satu dimensi, anggota ini harus ditentukan menjadi 1
        input_dims = 1
        output_dims = 1
        is_separable = True

        def __init__(self, thresh):
            mtransforms.Transform.__init__(self)
            self.thresh = thresh

        def transform_non_affine(self, a):
            """
            transformasi ini menghasilkan Nx1 array ``numpy``dan menghasilkan
            salinan transformasi. Karena jarak dari skala Mercator sudah dibatasi
            dengan pengendalian secara spesifik, masukan array harus dilengkapi
            dengan nilai yang benar ``matplotlib``  akan mengatur kelengkapan array
            dan merubahnya diluar dari jarak data pada plot.
            Yang terpenting, metode ``transform`` harus menghasilkan array dimana
            bentuknya seperti array masukan, karena nilai yang dibuthkan tersikronasi
            dengan nilai dalam dimensi lainnya
            """
            masked = ma.masked_where((a < -self.thresh) | (a > self.thresh), a)
            if masked.mask.any():
                return ma.log(np.abs(ma.tan(masked) + 1.0 / ma.cos(masked)))
            else:
                return np.log(np.abs(np.tan(a) + 1.0 / np.cos(a)))

        def inverted(self):
            return MercatorLatitudeScale.InvertedMercatorLatitudeTransform(self.thresh)

    class InvertedMercatorLatitudeTransform(mtransforms.Transform):
        input_dims = 1
        output_dims = 1
        is_separable = True

        def __init__(self, thresh):
            mtransforms.Transform.__init__(self)
            self.thresh = thresh

        def transform_non_affine(self, a):
            return np.arctan(np.sinh(a))

        def inverted(self):
            return MercatorLatitudeScale.MercatorLatitudeTransform(self.thresh)

#mendefinisikan kelas skala dan mengenalkannya, sehingga ``matplotlib`` dapat menemukannya
mscale.register_scale(MercatorLatitudeScale)

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    t = np.arange(-180.0, 180.0, 0.1)
    s = t / 360.0 * np.pi

    plt.plot(t, s, '-', lw=2)
    plt.gca().set_yscale('mercator')

    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Mercator: Projek dari Oppressor')
    plt.grid(True)

    plt.show()

