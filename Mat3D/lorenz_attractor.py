# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

"""
Plot Lorenz Attractor didasarkan publikasi Edward Lorenz's 1963 
"Deterministic Nonperiodic Flow"
http://journals.ametsoc.org/doi/abs/10.1175/1520-0469%281963%29020%3C0130%3ADNF%3E2.0.CO%3B2
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def lorenz(x, y, z, s=10, r=28, b=2.667):
	x_dot = s*(y-x)
	y_dot = r*x - y - x*z
	z_dot = x*y - b*z
	return x_dot, y_dot, z_dot
	
dt = 0.01
stepCnt = 10000

#membutuhkan lebih dari satu pengenalan nilai diawal
xs = np.empty((stepCnt + 1,))
ys = np.empty((stepCnt + 1,))
zs = np.empty((stepCnt + 1,))

#menentukan nilai pengenalan
xs[0], ys[0], zs[0] = (0., 1., 1.05)

for i in range(stepCnt) :
    #membentuk daerah X, Y, Z
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(xs, ys, zs)
ax.set_xlabel("Sumbu X")
ax.set_ylabel("Sumbu Y")
ax.set_zlabel("Sumbu Z")
ax.set_title("Lorenz Attractor")

plt.show()
