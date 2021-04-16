import numpy as np
import matplotlib.pyplot as plt

x = np.array([200, 300, 360, 480, 570, 770, 870, 950])
y = np.array([10, 15, 30, 40, 50, 70, 80, 100])
dx = 40
dy = 10

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax1.errorbar(x, y, xerr=dx, yerr=dy, marker='o', markersize=4, linestyle='', color='k',  ecolor='0.7', elinewidth=3, capsize=0, label='Recent activity of the CFC')
ax1.legend(loc='upper left')
ax1.set_xlabel('Zr [ppm]')
ax1.set_ylabel('Th [ppm]')

ax2 = fig.add_subplot(2,1,2)
ax2.errorbar(x, y, xerr=dx, yerr=dy, marker='o', markersize=6, linestyle='', color='#c7ddf4', markeredgecolor='k', ecolor='k', elinewidth = 0.8, capthick=0.8, capsize=3, label='Recent activity of the CFC')
ax2.legend(loc='upper left')
ax2.set_xlabel('Zr [ppm]')
ax2.set_ylabel('Th [ppm]')



