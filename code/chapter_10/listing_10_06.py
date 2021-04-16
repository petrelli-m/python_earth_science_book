import numpy as np
import matplotlib.pyplot as plt

x = np.array([250,300,360,480,570,770,870,950])
y = np.array([20,25,30,40,50,70,80,100])


fig = plt.figure(figsize=(6,8))

# xerr and yerr reported as single value
dx = 50
dy = 10
ax1 = fig.add_subplot(3,1,1)
ax1.errorbar(x, y, xerr=dx, yerr=dy, marker='o', markersize=6, linestyle = '', color='#c7ddf4', markeredgecolor='k', ecolor='0.7', label='single value for xerr and yerr')
ax1.legend(loc='upper left')

# xerr and yerr reported as 1D array
dx = np.array([25,35,40,120,150,30,30,25])
dy = np.array([8,8,6,7,7,35,40,40])

ax2 = fig.add_subplot(3,1,2)
ax2.errorbar(x, y, xerr=dx, yerr=dy, marker='o', markersize=6, linestyle = '', color='#c7ddf4', markeredgecolor='k', ecolor='0.7', label='xerr and yerr as 1D array')
ax2.set_ylabel('Th [ppm]')
ax2.legend(loc='upper left')

# xerr and yerr reported as 2D array
dx = np.array([[80,60,70,100,150,150,20,100],[20,25,30,30,30,30,90,30]])
dy = np.array([[10,4,10,15,15,20,5,5],[2,8,4,4,6,7,10,20]])

ax3 = fig.add_subplot(3,1,3)
ax3.errorbar(x, y, xerr=dx, yerr=dy, marker='o', markersize=6, linestyle = '', color='#c7ddf4', markeredgecolor='k', ecolor='0.7',  label='xerr and yerr as 2D array')
ax3.set_xlabel('Zr [ppm]')
ax3.legend(loc='upper left')

fig.tight_layout()