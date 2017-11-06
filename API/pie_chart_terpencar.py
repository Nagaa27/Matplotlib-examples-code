# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

import math
import numpy as np
import matplotlib.pyplot as plt

r1 = 0.2		#20 persen
r2 = r1 + 0.4	#40 persen
sizes = [60,80,120]

x = [0] + np.cos(np.linspace(0, 2*math.pi*r1, 10)).tolist()
y = [0] + np.sin(np.linspace(0, 2*math.pi*r1, 10)).tolist()
xy1 = list(zip(x,y))

x = [0] + np.cos(np.linspace(2*math.pi*r1, 2*math.pi*r2, 10)).tolist()
y = [0] + np.sin(np.linspace(2*math.pi*r1, 2*math.pi*r2, 10)).tolist()
xy2 = list(zip(x,y))

x = [0] + np.cos(np.linspace(2*math.pi*r2, 2*math.pi, 10)).tolist()
y = [0] + np.sin(np.linspace(2*math.pi*r2, 2*math.pi, 10)).tolist()
xy3 = list(zip(x,y))

fig, ax = plt.subplots()
ax.scatter(np.arange(3), np.arange(3), marker=(xy1,0), s=sizes, 
	facecolor = 'blue')
ax.scatter(np.arange(3), np.arange(3), marker=(xy2,0), s=sizes, 
	facecolor = 'green')
ax.scatter(np.arange(3), np.arange(3), marker=(xy3,0), s=sizes, 
	facecolor = 'red')
plt.show()
