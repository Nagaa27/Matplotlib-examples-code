# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

from __future__ import print_function
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.text import Text
from matplotlib.image import AxesImage
import numpy as np
from numpy.random import rand

if 1: #memilih lines, rectangles dan text
    fig, (ax1, ax2) = plt.subplots(2,1)
    ax1.set_title('click on points, rectangles or text', picker=True)
    ax1.set_ylabel('ylabel', picker=True, bbox=dict(facecolor='red'))
    line, = ax1.plot(rand(100), 'o', picker=5)  # 5 points tolerance

    #memilih rectangle
    bars = ax2.bar(range(10), rand(10), picker=True)
    # membuat the xtick labels dapat dipilih
    for label in ax2.get_xticklabels():  
        label.set_picker(True)
		
    def onpick1(event):
        if isinstance(event.artist, Line2D):
            thisline = event.artist
            xdata = thisline.get_xdata()
            ydata = thisline.get_ydata()
            ind = event.ind
            print('onpick1 line:', zip(np.take(xdata, ind), np.take(ydata, ind)))
        elif isinstance(event.artist, Rectangle):
            patch = event.artist
            print('onpick1 patch:', patch.get_path())
        elif isinstance(event.artist, Text):
            text = event.artist
            print('onpick1 text:', text.get_text())

    fig.canvas.mpl_connect('pick_event', onpick1)

if 1: #memilih dengan mengatur jumlah fungsi tes
	  #anda dapat mendefinisikan custom pickers dengan menentukan picker
	  #agar dapat dipanggil fungsi. fungsi memiliki pengenalan
	  #
	  #  hit, props = func(artist, mouseevent)
	  #
	  #untuk menentukan jumlah test, jika gerakan mouse berada pada hasil
	  # return hit=True dan props adalah kamus pada
      # properties anda inginkan untuk ditambahkan PickEvent attributes

	def line_picker(line, mouseevent):
		"""
		menentukan nilai dnegan kepastian jarak dari klikan mouse pada 
		kordinat data dan melampirkan beberapa lampiran tambahan, 
		pickx dan picky dimana terdapat data point yang dipilih
		"""
		if mouseevent.xdata is none: return False, dict()
		xdata = line.get_xdata()
		ydata = line.get_ydata()
		maxd = 0.05
		d = np.sqrt((xdata-mouseevent.xdata)**2. + (ydata-mouseevent.ydata)**2.)
		ind = np.nonzero(n.less_equal(d, maxd))
		if len (ind):
			pickx = np.take(xdata, ind)
			picky = np.take(ydata, ind)
			props = dict(ind=ind, pickx=pickx, picky=picky)
			return False, dict()
			
	def onpick2(event):
		print('onpick2 line:', event.pickx, event.picky)
	fig, ax = plt.subplots()
	ax.set_title('menentukan pemilihan pada baris data')
	line, = ax.plot(rand(100), rand(100), 'o', picker=line_picker)
	fig.canvas.mpl_connect('pick_event', onpick2)
	
if 1: #memilih plot yang betebaran (matplotlib.collections.RegularPolyCollection)
	x, y, c, s = rand(4, 100)
	def onpick3(event):
		ind = event.ind
		print('onpick3 scatter:', ind, np.take(x, ind), np.take(y, ind))
	fig, ax = plt.subplots()
	col = ax.scatter(x, y, 100*s, c, picker=True)
	#fig.savefig('pscoll.eps')
	fig.canvas.mpl_connect('pick_event', onpick3)
	
if 1 : #memilih gambar (matplotlib.image.AxesImage)
	fig, ax = plt.subplots()
	im1 = ax.imshow(rand(10,5), extent=(1,2,1,2), picker=True)
	im2 = ax.imshow(rand(5,10), extent=(3,4,1,2), picker=True)
	im3 = ax.imshow(rand(20,25), extent=(1,2,3,4), picker=True)
	im4 = ax.imshow(rand(30,12), extent=(3,4,3,4), picker=True)
	ax.axis([0,5,0,5])
	
	def onpick4(event):
		artist = event.artist
		if isinstance(artist, AxesImage):
			im = artist
			A = im.get_array()
			print('onpick4 image', A.shape)
	fig.canvas.mpl_connect('pick_event', onpick4)
plt.show()
	
