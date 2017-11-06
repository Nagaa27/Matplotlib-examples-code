# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

import matplotlib.pyplot as plt
labels = 'Matius', 'Celcius','Sinaga','Gan'
sizes = [15, 30, 45, 10]
colors = ['yellowgreen','gold','lightskyblue','lightcoral']
explode = (0, 0.1, 0, 0)
plt.pie (sizes, explode=explode, labels=labels, colors=colors, 
			autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()
