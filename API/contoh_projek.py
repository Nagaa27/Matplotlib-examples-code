# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

from __future__ import unicode_literals
import matplotlib
from matplotlib.axes import Axes
from matplotlib.patches import Circle
from matplotlib.path import Path
from matplotlib.ticker import NullLocator, Formatter, FixedLocator
from matplotlib.transforms import Affine2D, BboxTransformTo, Transform
from matplotlib.projections import register_projection
import matplotlib.spines as mspines
import matplotlib.axis as maxis
import numpy as np

#program ini adalah salah satu contoh yang memiliki listing lumayan panjang
#mengislustrasikan banyak fitur, namun tidak semua digunakan sekaligus
#ada beberapa faktor diluar dari penggunaan metode  dalam kode yang digunakan
#oleh beberapa projek yang karakternya sama
#http://en.wikipedia.org/wiki/Hammer_projection

class HammerAxes(Axes):
    name = 'custom_hammer'

    def __init__(self, *args, **kwargs):
        Axes.__init__(self, *args, **kwargs)
        self.set_aspect(0.5, adjustable='box', anchor='C')
        self.cla()

    def _init_axis(self):
        self.xaxis = maxis.XAxis(self)
        self.yaxis = maxis.YAxis(self)
        #xaxis dan yaxis tidak langsung di kenalkan pada kerangka
        #sebagaimana Axes._init_axis() -- until HammerAxes.xaxis.cla() bekerja
        # self.spines['hammer'].register_axis(self.yaxis)
        self._update_transScale()

    def cla(self):
        #tidak menentukan hasil langsung
        Axes.cla(self)

        #menentukan jarak pada pengaturan umum
        self.set_longitude_grid(30)
        self.set_latitude_grid(15)
        self.set_longitude_grid_ends(75)

        #menonaktifkan tempat yang tidak sesuai
        self.xaxis.set_minor_locator(NullLocator())
        self.yaxis.set_minor_locator(NullLocator())

        #hanya menampilkan garis dan teks
        self.xaxis.set_ticks_position('none')
        self.yaxis.set_ticks_position('none')

        #batasan pada projek ini sudah ditentukan dan tak bisa dirubah pengguna
        #dimana akan meringankan perhitungan dalam bertransformasi dengan sendirinya
        #lebih mudah dan bahkan lebih baik
        Axes.set_xlim(self, -np.pi, np.pi)
        Axes.set_ylim(self, -np.pi / 2.0, np.pi / 2.0)

    def _set_lim_and_transforms(self):
        """
        Hanya akan berlangsung sekali saja ketika plot/alur sudah 
        menentukan pengaturan umum pada transformasi pada, teks dan tempat
        """
        #	Ada beberapa bagian yang harus anda ketahui :
        #1. Data space 		: ruang pada data itu sendiri
        #2. Axes space 		: unit segiempat (0, 0) to (1, 1) untuk 
        #				 	  melengkapi area masukan
        #3. Display space 	: kordinat yang dihasilkan pada gambar
        #       			   biasanya dalam pixel atau dpi/inch
        #
        #fungsi ini lumayan berat pada transformasi kelas dalam
        # ``lib/matplotlib/transforms.py.`` 
		#tujuan dari transformasi awal kedua transformasi adalah menetapkan
		#data space dalam hal ini adalah longitude dan latitude pada ruang sumbu
		#hal ini kemudian dibagi menjadi non-affine dan affine yang dimaksud dengan
		#non-affine adalah dimana tidak ada perhitungan kembali ketika
		#affine sudah dirubah menjadi gambar yang sudah jadi seperti 
		#merubah ukuran tampilan dan mengubah dpi
		#
        # 1) Inti transfrmasi dari data space menjadi rectilinear space
        #sudah dijelaskan dalam kelas HammerTransform
        self.transProjection = self.HammerTransform()

        # 2) Rentang hasil keluaran sebelumnya bukan dalam segiempat unit
        #maka skala dan juga penerjemahannya menjadi cocok dengan sumbu
        #perhitungan yang unik pada xscale dan yscale spesifik pada
        #projek Aitoff-Hammer maka tidak usah ragu
        xscale = 2.0 * np.sqrt(2.0) * np.sin(0.5 * np.pi)
        yscale = np.sqrt(2.0) * np.sin(0.5 * np.pi)
        self.transAffine = Affine2D() \
            .scale(0.5 / xscale, 0.5 / yscale) \
            .translate(0.5, 0.5)

        # 3) Menstransformasikan dari ruang sumbu pada ruang tampilan
        self.transAxes = BboxTransformTo(self.bbox)

        #tambahkan ke 3 transormasi ini bersama-sama dari seluruh data
        #untuk mencapai tampilan kordinat menggunakan operator '+' ,
        #ditransformasi menjadi "in order". Transformasi secara otomatis
        #sangatlah sederhana, kalaupun bisa dengan dasar framework transformasi
        self.transData = \
            self.transProjection + \
            self.transAffine + \
            self.transAxes

        #data utama transformasi sudah ditentukan
        #maka sekarang tentukan gridlines and tick labels.
        #Longitude gridlines dan ticklabels. Masukan pada transformasi
        #dalam display space x and sumbu ruang y.
        #Maka, nilai masukan dalam rentang(-xmin, 0), (xmax, 1)
        #Tujuan akhir dari transformasi ini adalah mencapai ruang display space
        #ketebalan label akan menjadi offset 4 pixels dari the equator
        self._xaxis_pretransform = \
            Affine2D() \
            .scale(1.0, np.pi) \
            .translate(0.0, -np.pi)
        self._xaxis_transform = \
            self._xaxis_pretransform + \
            self.transData
        self._xaxis_text1_transform = \
            Affine2D().scale(1.0, 0.0) + \
            self.transData + \
            Affine2D().translate(0.0, 4.0)
        self._xaxis_text2_transform = \
            Affine2D().scale(1.0, 0.0) + \
            self.transData + \
            Affine2D().translate(0.0, -4.0)

        #menentukan ketebalan latitude. Masukan pada transformasi dalam 
        #sumbu ruang pada x dan display space pada y. Selanjutnya, 
        #masukan pada transformasidalam display space x and sumbu ruang y.
        #Maka, nilai masukan dalam rentang(-xmin, 0), (xmax, 1)
        #Tujuan akhir dari transformasi ini adalah mencapai ruang display space
        #ketebalan label akan menjadi offset 4 pixels dari the equator
        yaxis_stretch = Affine2D().scale(np.pi * 2.0, 1.0).translate(-np.pi, 0.0)
        yaxis_space = Affine2D().scale(1.0, 1.1)
        self._yaxis_transform = \
            yaxis_stretch + \
            self.transData
        yaxis_text_base = \
            yaxis_stretch + \
            self.transProjection + \
            (yaxis_space + \
             self.transAffine + \
             self.transAxes)
        self._yaxis_text1_transform = \
            yaxis_text_base + \
            Affine2D().translate(-8.0, 0.0)
        self._yaxis_text2_transform = \
            yaxis_text_base + \
            Affine2D().translate(8.0, 0.0)

    def get_xaxis_transform(self,which='grid'):
        #menyediakan sebuah transformasi pada x-axis grid and ticks
        assert which in ['tick1','tick2','grid']
        return self._xaxis_transform

    def get_xaxis_text1_transform(self, pixelPad):
        #menyediakan sebuah transformasi pada x-axis grid dan ticks labels.
        #Returns a tuple of the form (transform, valign, halign)
        return self._xaxis_text1_transform, 'bottom', 'center'

    def get_xaxis_text2_transform(self, pixelPad):
        #menyediakan sebuah transformasi pada x-axis kedua ticks labels.
        #Returns a tuple of the form (transform, valign, halign)
        return self._xaxis_text2_transform, 'top', 'center'

    def get_yaxis_transform(self,which='grid'):
        #menyediakan sebuah transformasi pada y-axis grid and ticks labels.
        assert which in ['tick1','tick2','grid']
        return self._yaxis_transform

    def get_yaxis_text1_transform(self, pixelPad):
        #menyediakan sebuah transformasi pada y-axisticks labels.
        #Returns a tuple of the form (transform, valign, halign)
        return self._yaxis_text1_transform, 'center', 'right'

    def get_yaxis_text2_transform(self, pixelPad):
        #menyediakan sebuah transformasi pada y-axis kedua ticks labels.
        #Returns a tuple of the form (transform, valign, halign)
        return self._yaxis_text2_transform, 'center', 'left'

    def _gen_axes_patch(self):
        #lingkaran/circle, setiap data dan gridline akan di bentuk 
        return Circle((0.5, 0.5), 0.5)

    def _gen_axes_spines(self):
        return {'custom_hammer':mspines.Spine.circular_spine(self,
                                                      (0.5, 0.5), 0.5)}

    #mencegah pengguna untuk menerapkan skala pada salah satu atau kedua sumbu
    #dalam hal khusus ini, penskalaan tidak memberi efek maka dibatasi
    def set_xscale(self, *args, **kwargs):
        if args[0] != 'linear':
            raise NotImplementedError
        Axes.set_xscale(self, *args, **kwargs)

    def set_yscale(self, *args, **kwargs):
        if args[0] != 'linear':
            raise NotImplementedError
        Axes.set_yscale(self, *args, **kwargs)

    #mencegah pengguna dari perubahan batas sumbu, dalam hal ini kita 
    #inginkan untuk menampilkan seluruh bagian(bulat), dan juga pada
    #set_xlim dan set_ylim menolak segalamasukan. Hal ini juga diterapkan
    #dalam min dan max interaksi GUI
    def set_xlim(self, *args, **kwargs):
        Axes.set_xlim(self, -np.pi, np.pi)
        Axes.set_ylim(self, -np.pi / 2.0, np.pi / 2.0)
    set_ylim = set_xlim

    def format_coord(self, lon, lat):
        #menampilkan derajat dalam setiap kutub N/S/E/W
        lon = lon * (180.0 / np.pi)
        lat = lat * (180.0 / np.pi)
        if lat >= 0.0:
            ns = 'N'
        else:
            ns = 'S'
        if lon >= 0.0:
            ew = 'E'
        else:
            ew = 'W'
        # \u00b0 : degree symbol
        return '%f\u00b0%s, %f\u00b0%s' % (abs(lat), ns, abs(lon), ew)

    class DegreeFormatter(Formatter):
        #membentuk format yang mengubah unit native pada radian menjadi
        #derajat dan menambahkan simbol derajat
        def __init__(self, round_to=1.0):
            self._round_to = round_to

        def __call__(self, x, pos=None):
            degrees = (x / np.pi) * 180.0
            degrees = round(degrees / self._round_to) * self._round_to
            # \u00b0 : degree symbol
            return "%d\u00b0" % degrees

    def set_longitude_grid(self, degrees):
		#menentukan jumlah dari derajat diantara tiap longitude grid
		#pada contoh metode ini bahwa secara spesifik pada kelas projek
		#memberikan antarmuka yang baik untuk menentukan set_xticks nantinya
		#menentukan FixedLocator pada tiap titik, bahkan ruang dengan derajat
        number = (360.0 / degrees) + 1
        self.xaxis.set_major_locator(
            plt.FixedLocator(
                np.linspace(-np.pi, np.pi, number, True)[1:-1]))
        #menentukan format pada tampilan ketebalan label dalam derajat bahkan radian
        self.xaxis.set_major_formatter(self.DegreeFormatter(degrees))

    def set_latitude_grid(self, degrees):
		#menentukan jumlah dari derajat diantara tiap longitude grid
		#pada contoh metode ini bahwa secara spesifik pada kelas projek
		#memberikan antarmuka yang baik untuk menentukan set_yticks nantinya
        #menentukan FixedLocator pada tiap titik, bahkan ruang dengan derajat
        number = (180.0 / degrees) + 1
        self.yaxis.set_major_locator(
            FixedLocator(
                np.linspace(-np.pi / 2.0, np.pi / 2.0, number, True)[1:-1]))
        #menentukan format pada tampilan ketebalan label dalam derajat bahkan radian
        self.yaxis.set_major_formatter(self.DegreeFormatter(degrees))

    def set_longitude_grid_ends(self, degrees):
        #menentukan latitude dimana akan berhenti menggambar longitude grid
        #biasanya dalam projek geografi, anda tidak akan menggambar longitude gridlines
        #mendekati pola. Akan memberikan pengguna derajat secara spesifik 
        #pada saat berhenti menggambar longitude grid
        #contoh metode ini secara spesifik pada kelas projek
        #dan menyatakan bahwa antarmuka pada sesuatu yang tidak memiliki
        #analogy dalam dasar sumbu kelas
        longitude_cap = degrees * (np.pi / 180.0)
        #merubah transformasi xaxis gridlines maka akan menggambarakan
        #derajat demi derajat juga -pi ke pi.
        self._xaxis_pretransform \
            .clear() \
            .scale(1.0, longitude_cap * 2.0) \
            .translate(0.0, -longitude_cap)

    def get_data_ratio(self):
		#menghasilkan rasio aspek pada data itu sendiri
		return 1.0

    #min dan max tidak didukung pada projek kali ini 
    #maka metode yang berhubungan akan didisable
    def can_zoom(self):
        #menghasilkan True jika sumbu didukung pada kotak pembesaran
        return False
    def start_pan(self, x, y, button):
        pass
    def end_pan(self):
        pass
    def drag_pan(self, button, key, x, y):
        pass

    #transformasi dengan sendirinya
    class HammerTransform(Transform):
        #dasar Hammer transform
        input_dims = 2
        output_dims = 2
        is_separable = False

        def transform_non_affine(self, ll):
            #masukannya adalah Nx2 numpy arrays
            longitude = ll[:, 0:1]
            latitude  = ll[:, 1:2]

            #sebelum menghitung beberapa nilai
            half_long = longitude / 2.0
            cos_latitude = np.cos(latitude)
            sqrt2 = np.sqrt(2.0)
            alpha = 1.0 + cos_latitude * np.cos(half_long)
            x = (2.0 * sqrt2) * (cos_latitude * np.sin(half_long)) / alpha
            y = (sqrt2 * np.sin(latitude)) / alpha
            return np.concatenate((x, y), 1)

        #garis lurus dalam data space menjadi kurva dalam display space
        #dengan interpolasi nilai baru diantara masukan nilai pada data
        #karena "transformasi" tidak harus menghasilkan ukuran array 
        #yang berbeda, setiap transform akan membutuhkan perubahan panjang
        #pada data array yang terjadi dalam ``transform_path``.
        def transform_path_non_affine(self, path):
            ipath = path.interpolated(path._interpolation_steps)
            return Path(self.transform(ipath.vertices), ipath.codes)
        transform_path_non_affine.__doc__ = \
                Transform.transform_path_non_affine.__doc__

        if matplotlib.__version__ < '1.2':
            #cocok dengan matplotlib v1.1 dan sebelumnya, anda harus secara
            #eksplisit mengimplementasikan sebuah metode ``transform``
            #sebaik mungkin. Apabila sebuah ``NotImplementedError`` didapat
            #hal ini bahkan tidak mendekati v1.2 dan yang terbaru
            transform = transform_non_affine

            #jika ``transform_path`` cocok dengan matplotlib yang lebih lawas
            #versi yang dibutuhkan adalah v1.2 dan yang terbaru
            transform_path = transform_path_non_affine
            transform_path.__doc__ = Transform.transform_path.__doc__

        def inverted(self):
            return HammerAxes.InvertedHammerTransform()
        inverted.__doc__ = Transform.inverted.__doc__

    class InvertedHammerTransform(Transform):
        input_dims = 2
        output_dims = 2
        is_separable = False

        def transform_non_affine(self, xy):
            x = xy[:, 0:1]
            y = xy[:, 1:2]

            quarter_x = 0.25 * x
            half_y = 0.5 * y
            z = np.sqrt(1.0 - quarter_x*quarter_x - half_y*half_y)
            longitude = 2 * np.arctan((z*x) / (2.0 * (2.0*z*z - 1.0)))
            latitude = np.arcsin(y*z)
            return np.concatenate((longitude, latitude), 1)
        transform_non_affine.__doc__ = Transform.transform_non_affine.__doc__

        #seperti sebelumnya, kita harus mengimplementasikan metode "transform"
        #cocok dengan  matplotlib v1.1 dan yang lawas
        if matplotlib.__version__ < '1.2':
            transform = transform_non_affine

        def inverted(self):
            #kebalikan dari kebalikan adalah transformasi yang asli
            return HammerAxes.HammerTransform()
        inverted.__doc__ = Transform.inverted.__doc__

#daftarkan projek dengan matplotlib maka penggunadapat memilih
register_projection(HammerAxes)

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    plt.subplot(111, projection="custom_hammer")
    p = plt.plot([-1, 1, 1], [-1, -1, 1], "o-")
    plt.grid(True)

    plt.show()

