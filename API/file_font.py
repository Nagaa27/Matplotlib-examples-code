# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 


#meskipun hal ini biasanya bukanlah ide yang bagus untuk mengeksplisitkan 
#nilai pada satu file ttf  pada font contoh, anda dapat menggunakan 
#font_manager.FontProperties fname argumen 

import sys
import os
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1,2,3])

#pada windows, menjelaskan path yang digunakan
if sys.platform == 'win32':
	fpath = 'C:\\Windows\\Fonts\\Tahoma.ttf'
elif sys.platform.startswith('linux'):
	fonts = ['/usr/share/fonts/truetype/freefont/FreeSansBoldOblique.ttf',
	'/usr/share/fonts/truetype/ttf-liberation/LiberationSans-BoldItalic.ttf'
	'/usr/share/fonts/truetype/msttcorefonts/Comic_Sans_MS.ttf',
	]
	for fpath in fonts:
		if os.path.exists(fpath):
			break
else:
	fpath = '/Library/Fonts/Tahoma.ttf'
	
if os.path.exists(fpath):
	prop = fm.FontProperties(fname=fpath)
	fname = os.path.split(fpath)[1]
	ax.set_title('Ini adalah font spesial : %s' % fname, fontproperties=prop)
else:
	#apabila demo gagal dan default
	ax.set_title('Demo gagal--tidak dapat menemukan sebuah font demo')
	ax.set_xlabel('Ini adalah font default')
	
plt.show()

