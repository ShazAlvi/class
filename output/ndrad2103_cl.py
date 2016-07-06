import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/n/home12/rebecca.krall/class1/output/ndrad2103_cl.dat', '/n/home12/rebecca.krall/class1/output/mp_lcdm01_cl.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['ndrad2103_cl', 'mp_lcdm01_cl']

fig, ax = plt.subplots()
y_axis = [u'EE']
tex_names = ['EE']
x_axis = 'l'
ax.set_xlabel('$\ell$', fontsize=16)
plt.show()