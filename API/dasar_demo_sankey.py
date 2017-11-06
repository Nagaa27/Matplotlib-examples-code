# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

Sankey(flows=[0.25, 0.15, 0.60, -0.20, -0.15, -0.05, -0.50, -0.10],
       labels=['', '', '', 'Pertama', 'Kedua', 'Ketiga', 'Keempat', 'Kelima'],
       orientations=[-1, 1, 0, 1, 1, 1, 0, -1]).finish()
plt.title("PEngaturan secara umum untuk menghasilkan diagram seperti ini.")
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[], title="Diagram alur pada layar")
sankey = Sankey(ax=ax, scale=0.01, offset=0.2, head_angle=180,
                format='%.0f', unit='%')
sankey.add(flows=[25, 0, 60, -10, -20, -5, -15, -10, -40],
           labels = ['', '', '', 'Pertama', 'Kedua', 'Ketiga', 'Keempat',
                     'Kelima', 'Ohh.. yeah!'],
           orientations=[-1, 1, 0, 1, 1, 1, -1, -1, 0],
           pathlengths = [0.25, 0.25, 0.25, 0.25, 0.25, 0.6, 0.25, 0.25,
                          0.25],
           patchlabel="Widget\nA",
           alpha=0.2, lw=2.0) # Arguments pada matplotlib.patches.PathPatch()
diagrams = sankey.finish()
diagrams[0].patch.set_facecolor('#37c959')
diagrams[0].texts[-1].set_color('r')
diagrams[0].text.set_fontweight('bold')
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[], title="Dua Sistem")
flows = [0.25, 0.15, 0.60, -0.10, -0.05, -0.25, -0.15, -0.10, -0.35]
sankey = Sankey(ax=ax, unit=None)
sankey.add(flows=flows, label='Satu',
           orientations=[-1, 1, 0, 1, 1, 1, -1, -1, 0])
sankey.add(flows=[-0.25, 0.15, 0.1], fc='#37c959', label='Dua',
           orientations=[-1, -1, -1], prior=0, connect=(0, 0))
diagrams = sankey.finish()
diagrams[-1].patch.set_hatch('/')
plt.legend(loc='best')
#untuk diketahui bahwa hanya satu penghubung yang dikhususkan. Pada aliran
#dapat dilihat : 1. Panjang dari tempat yang seimbang | 2. Aliran yang mengalir
#dan tujuannya
plt.show()

