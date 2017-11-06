# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

import numpy as np
import matplotlib.pyplot as plt

N = 5
menMeans = (20, 35, 30, 35, 27)
menStd = (2, 3, 4, 1, 2)
ind = np.arange(N)	#lokasi x pada grup
width = 0.35		#ukuran pada bar

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)

womenMeans = (25, 32, 34, 20, 25)
womenStd = (3, 5, 2, 3, 3)
rects2 = ax.bar(ind+width, womenMeans, width, color='y', yerr=womenStd)

#tambahkan beberapa teks pada label, judul dan ketebalan sumbu
ax.set_ylabel('Scores')
ax.set_title('Scores dengan grup dan gender')
ax.set_xticks(ind+width)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))

ax.legend ((rects1[0], rects2[0]), ('Men', 'Women'))

def autolabel(rects):
	#lampirkan beberapa label teks
	for rect in rects:
		height = rect.get_height()
		ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, 
		'%d'%int(height), ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)

plt.show()
