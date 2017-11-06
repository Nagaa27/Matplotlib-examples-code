# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes([0.1, 0.3, 0.5, 0.5])
ax.pcolormesh(np.array([[1,2], [3,4]]))
plt.yticks([0.5, 1.5], ["long long tick label",
						"tick label"])
plt.ylabel("My y-label")
plt.title("Gambar Kotak-kotak sudah Tersimpan")
for ext in ["png", "pdf", "svg", "svgz", "eps"]:
    print("saving tight_bbox_test.%s" % (ext,))
    plt.savefig("tight_bbox_test.%s" % (ext,), bbox_inches="tight")
plt.show()
