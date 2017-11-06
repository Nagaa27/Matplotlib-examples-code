# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

"""
Saat mouse bergerak dalam segitiga akan ditandai dan dikenal lalu 
menghasilkan nilai pengembalian(identitas) daerah yang ditandai
"""
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation
from matplotlib.patches import Polygon
import numpy as np
import math

def update_polygon(tri):
	if tri == -1:
		points = [0, 0, 0]
	else:
		points = triangulation.triangles[tri]
	xs = triangulation.x[points]
	ys = triangulation.y[points]
	polygon.set_xy(zip(xs, ys))
	
def motion_notify(event):
	if event.inaxes is None:
		tri = -1
	else:
		tri = trifinder(event.xdata, event.ydata)
	update_polygon(tri)
	plt.title('Dalam segitiga %i' % tri)
	event.canvas.draw()

#membuat triangulasi
n_angles = 16
n_radii = 5
min_radius = 0.25
radii = np.linspace(min_radius, 0.95, n_radii)
angles = np.linspace(0, 2*math.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += math.pi / n_angles
x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
triangulation = Triangulation(x, y)
xmid = x[triangulation.triangles].mean(axis=1)
ymid = y[triangulation.triangles].mean(axis=1)
mask = np.where(xmid*xmid + ymid*ymid < min_radius*min_radius, 1, 0)
triangulation.set_mask(mask)

#menggunakan triangulasi sebagai pengaturan umum objek TriFinder
trifinder = triangulation.get_trifinder()

#menentukan plot dan memamnggilnya kembali
plt.subplot(111, aspect='equal')
plt.triplot(triangulation, 'bo-')
polygon = Polygon([[0,0], [0,0]], facecolor='y')
plt.gca().add_patch(polygon)
plt.gcf().canvas.mpl_connect('motion_notify_event', motion_notify)
plt.show()
