# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

"""
Anda dapat secara eksplisit menentukan mana font family yang akan diambil 
untuk dijadikan tipe font misal 'serif', 'sans-serif' atau 'monoscape')
Dalam contoh berikut, kita hanya mengijinkan satu font saja yaitu Tahoma 
untuk san-serif font style. Anda menentukan font dengan font.family rcparam
	rcParams['font.family'] = 'sans-serif'
dan font.family ditentukan pada gaya penulisan untuk mencoba menemukan perintah :

	rcParams['font.sans-serif'] = ['Tahoma', 'Bitstream Vera Sans', 
	'Lucida Grande', 'Verdana']
"""

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Tahoma']
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1,2,3], label='test')

ax.legend()
plt.show()
