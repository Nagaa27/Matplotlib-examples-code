# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

#mendemonstrasikan apabila chart yang dihasilkan horizontal
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#silahkan ubah
people =('Kakek Sugiono', 'Amin Richman', 'GoodGuy Greg', 'Chuck Noris', 'MadDog')
y_pos = np.arange(len(people))

#chart yang dihasilkan akan berbeda-beda setiap tampilan
#rand
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))
plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
plt.yticks(y_pos, people)
plt.xlabel('Ketamfanannn')
plt.title('Seberapa ganteng anda ?')
plt.show()
