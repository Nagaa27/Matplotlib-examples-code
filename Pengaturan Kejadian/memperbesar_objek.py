# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

"""
Program ini akan menghubungkan kejadian antar jendela, contohnya adalah
saat anda menekan/mengklik objek akan diperjelas di jendela yang lain
"""
from matplotlib.pyplot import figure, show
import numpy
figsrc = figure()
figzoom = figure()

axsrc = figsrc.add_subplot(111, xlim=(0,1), ylim=(0,1), autoscale_on=False)
axzoom = figzoom.add_subplot(111, xlim=(0.45,0.55), ylim=(0.4,.6),
                                                    autoscale_on=False)
axsrc.set_title('Klik untuk memperbesar')
axzoom.set_title('Hasil perbesaran')
x,y,s,c = numpy.random.rand(4,200)
s *= 200


axsrc.scatter(x,y,s,c)
axzoom.scatter(x,y,s,c)

def onpress(event):
    if event.button!=1: return
    x,y = event.xdata, event.ydata
    axzoom.set_xlim(x-0.1, x+0.1)
    axzoom.set_ylim(y-0.1, y+0.1)
    figzoom.canvas.draw()

figsrc.canvas.mpl_connect('button_press_event', onpress)
show()

