# Matius Celcius Sinaga
# Ubuntu 14.0 | 32 bit 
# Python 2.7
# matplotlib-1.4.0 

"""
Mendemonstrasikan penyaringan SVG dimana digunakan mpl
penyaringan efek hanya akan efektif apabila svg didukung 
"""


import matplotlib
matplotlib.use("Svg")

import matplotlib.pyplot as plt
from matplotlib.patches import Shadow

#membuat sebuah gambar dan sumbu persegi
fig1 = plt.figure(1, figsize=(6,6))
ax = fig1.add_axes([0.1, 0.1, 0.8, 0.8])

labels = 'Bryan', 'Greg', 'Herp', 'Yaoming'
fracs = [15,30,45, 10]

explode=(0, 0.05, 0, 0)

#kita ingin menggambarkan bayangan pada tiap pie namun tidak menggunakan "shadow"
pies = ax.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%')

for w in pies[0]:
    #menentukan identitas degan label
    w.set_gid(w.get_label())

    #tidak harus menggambarkan akhir dari pie
    w.set_ec("none")

for w in pies[0]:
    #membuat shadow patch
    s = Shadow(w, -0.01, -0.01)
    s.set_gid(w.get_gid()+"_shadow")
    s.set_zorder(w.get_zorder() - 0.1)
    ax.add_patch(s)
    

# save
from StringIO import StringIO
f = StringIO()
plt.savefig(f, format="svg")

import xml.etree.cElementTree as ET


#mendefinisikan bayangan dengan menggunakan gaussian blur dan lighteneing effect
#lightnening filter disalin dari from http://www.w3.org/TR/SVG/filters.html
filter_def = """
  <defs  xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>
    <filter id='dropshadow' height='1.2' width='1.2'>
      <feGaussianBlur result='blur' stdDeviation='2'/>
    </filter>
    
    <filter id='MyFilter' filterUnits='objectBoundingBox' x='0' y='0' width='1' height='1'>
      <feGaussianBlur in='SourceAlpha' stdDeviation='4%' result='blur'/>
      <feOffset in='blur' dx='4%' dy='4%' result='offsetBlur'/>
      <feSpecularLighting in='blur' surfaceScale='5' specularConstant='.75' 
           specularExponent='20' lighting-color='#bbbbbb' result='specOut'>
        <fePointLight x='-5000%' y='-10000%' z='20000%'/>
      </feSpecularLighting>
      <feComposite in='specOut' in2='SourceAlpha' operator='in' result='specOut'/>
      <feComposite in='SourceGraphic' in2='specOut' operator='arithmetic' 
    k1='0' k2='1' k3='1' k4='0'/>
    </filter>
  </defs>
"""


tree, xmlid = ET.XMLID(f.getvalue())

#memasukkan penyaringan definisi dalam svg dom tree.
tree.insert(0, ET.XML(filter_def))

for i, pie_name in enumerate(labels):
    pie = xmlid[pie_name]
    pie.set("filter", 'url(#MyFilter)')

    shadow = xmlid[pie_name + "_shadow"]
    shadow.set("filter",'url(#dropshadow)')

fn = "svg_filter_pie.svg"
print "Saving '%s'" % fn
ET.ElementTree(tree).write(fn)
