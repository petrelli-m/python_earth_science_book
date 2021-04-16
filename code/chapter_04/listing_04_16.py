import matplotlib.pyplot as plt
import numpy as np


def ec(f, d, c0):
    cl = c0 / (d * (1-f) + f)
    return cl


my_f = np.linspace(0.1, 1, 10)

my_c1 = ec(f=my_f, d=0.1, c0=100)

colors = ['#ff9494', '#cbeaa2', '#d1a396', '#828fc3', '#95b2e5', '#e9b8f4', '#f4b8e5', '#b8f4f2', '#c5f4b8', '#f9ca78']

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(my_f, my_c1, marker='o', linestyle='-', markersize=5)
ax1.set_xlabel('F')
ax1.set_ylabel('C [ppm]')

ax2 = fig.add_subplot(2, 2, 2)
ax2.scatter(my_f, my_c1, marker='o', s=my_f*150)
ax2.set_xlabel('F')
ax2.set_ylabel('C [ppm]')

ax3 = fig.add_subplot(2, 2, 3)
ax3.scatter(my_f, my_c1, marker='o', c=colors, s=my_f*150)
ax3.set_xlabel('F')
ax3.set_ylabel('C [ppm]')

ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(my_f, my_c1, marker='', linestyle='-', zorder=0)
ax4.scatter(my_f, my_c1, marker='o', c=colors, s=my_f*150, zorder=1)
ax4.set_xlabel('F')
ax4.set_ylabel('C [ppm]')

fig.tight_layout()
