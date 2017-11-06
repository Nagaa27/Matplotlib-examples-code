# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

#sumber : http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.imshow
import matplotlib.pyplot as plt
import numpy as np

methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
           'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
           'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']

grid = np.random.rand(4, 4)
fig, axes = plt.subplots(3, 6, figsize=(12, 6),
                         subplot_kw={'xticks': [], 'yticks': []})
fig.subplots_adjust(hspace=0.3, wspace=0.05)
for ax, interp_method in zip(axes.flat, methods):
	ax.imshow(grid, interpolation=interp_method)
	ax.set_title(interp_method)
plt.show()
