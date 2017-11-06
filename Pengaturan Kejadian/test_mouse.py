# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

from __future__ import print_function
import matplotlib
import matplotlib.pyplot as plt
def OnClick(event):
	if event.dblclick:
		print("DOUBLE CLICK", event)
	else:
		print("DOWN ",event)
		
def OnRelease(event):
	print("UP ", event)
fig = plt.gcf()
cid_up = fig.canvas.mpl_connect('button_pres_event', OnClick)
cid_down = fig.canvas.mpl_connect('button_release_event', OnRelease)
plt.gca().text(0.5, 0.5, "Klik pada kotak posisi nilai muncul pada terminal.",
		ha="center", va="center")
plt.show()
	
