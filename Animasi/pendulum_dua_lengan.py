# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 
#program ini terjemahan dari kode C, Sumber :
#http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c

from numpy import sin, cos, pi, array
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

G = 9.8 	#gravitasi pada bumi, m/s^2
L1 = 1.0 	#panjang dari pendulum 1 dalam m
L2 = 1.0	#panjang dari pendulum 2 dalam m
M1 = 1.0	#berat dari pendulum 1 dalam kg
M2 = 1.0	#berat dari pendulum 2 dalam kg

def derivs(state, t):
	dydx = np.zeros_like(state)
	dydx[0] = state[1]
	del_ = state[2]-state[0]
	den1 = (M1+M2)*L1 - M2*L1*cos(del_)*cos(del_)
	dydx[1] = (M2*L1*state[1]*state[1]*sin(del_)*cos(del_) 
				+M2*G*sin(state[2])*cos(del_) + 
				M2*L2*state[3]*state[3]*sin(del_) - 
				(M1+M2)*G*sin(state[0]))/den1
	dydx[2] = state[3]
	den2 = (L2/L1)*den1
	dydx[3]= (-M2*L2*state[3]*state[3]*sin(del_)*cos(del_)
				+ (M1+M2)*G*sin(state[0])*cos(del_)
				- (M1+M2)*L1*state[1]*state[1]*sin(del_)
				- (M1+M2)*G*sin(state[2]))/den2
	
	return dydx

#membuat sebuah array waktu dari contoh 0..100 
#contoh diberikan 0.05 detik / gerakan
#diberikan waktu 27 detik
dt = 0.05
t = np.arange(0.0, 27, dt)

#th1 dan th2 adalah sudut awal (dalam derajat)
#w10 dan w20 memiliki kecepatan konstan (dalam detik)
th1 = 120.0
w1 = 0.0
th2 = -10.0
w2 = 0.0

rad = pi/180

#mengenalkan keadaan
state = np.array([th1, w1, th2, w2])*pi/180

#mencoba mengintegrasikan
y = integrate.odeint(derivs, state, t)
x1 = L1*sin(y[:,0])
y1 = -L1*cos(y[:,0])
x2 = L2*sin(y[:,2]) + x1
y2 = -L2*cos(y[:,2]) + y1
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    line.set_data(thisx, thisy)
    time_text.set_text(time_template%(i*dt))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)),
    interval=25, blit=True, init_func=init)

	
#ani.save('pendulum_dua_lengan.mp4', fps=15)
plt.show()
