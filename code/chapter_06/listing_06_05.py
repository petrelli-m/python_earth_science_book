import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(r, r0, D0, E): 
    R=8.314462618
    scale = 1e-21 # r in Angstrom (r^3 -> 10^-30 m), E is GPa (10^9 Pa)
    T = 800 + 273.15
    Na=6.02e23
    return D0*np.exp((-4*np.pi*E*Na*((r0/2)*(r-r0)**2+(1/3)*(r-r0)**3)*scale)/(R*T))

def add_elements(ax):
    # to plot the name of the elements on the diagram
    names = ['La', 'Ce', 'Nd', 'Sm', 'Eu', 'Gd', 'Dy', 'Er', 'Yb', 'Lu', 'Y', 'Sc']
    annotate_xs = np.array([1.172 + 0.01, 1.15 + 0.01, 1.123 + 0.01, 1.098 - 0.031, 1.087 - 0.028, 1.078 - 0.04, 1.052 + 0.005, 1.03 + 0.02, 1.008 + 0.01, 1.001 - 0.015, 1.04 -0.02, 0.885 - 0.03])
    annotate_ys = np.array([0.468 + 0.1, 1.050 + 0.2, 10.305 + 3,	31.283 - 13,	45.634 -17,	74.633- 30, 229.279 + 80, 485.500, 583.828 +200, 460.404 -220, 172.844 -70, 141.630])
    
    for name, annotate_x, annotate_y in zip(names, annotate_xs, annotate_ys):
        ax.annotate(name, (annotate_x, annotate_y))

Di = np.array([0.468, 1.050, 10.305,	31.283,	45.634,	74.633, 229.279, 485.500, 583.828, 460.404, 172.844, 141.630])
I_r = np.array([1.172, 1.15, 1.123, 1.098, 1.087, 1.078, 1.052, 1.03, 1.008, 1.001, 1.04, 0.885])

fig = plt.figure(figsize=(9,5))

# Trust Region Reflective algorithm
ax1 = fig.add_subplot(1,2,1)
ax1.set_title("Trust Region Reflective algorithm")
ax1.scatter(I_r, Di, s=80, color='#c7ddf4', edgecolors='k', label='4 GPa - 1073 K, Kessel et al., 2005')

popt1, pcov1 = curve_fit(func, I_r, Di, method='trf', bounds=([0.8,0,0],[1.3,1000,1000]))

x1 = np.linspace(0.85,1.2,1000)
y1 = func(x1,popt1[0],popt1[1], popt1[2])
ax1.plot(x1,y1, color='#ff464a', linewidth=2, linestyle ='--', label=r'$r_0$ = ' + str(round(popt1[0],3)) + r', $D_0$ = ' + str(round(popt1[1],0)) + ', E = ' + str(round(popt1[2],0)))
add_elements(ax = ax1)
ax1.set_yscale('log')
ax1.set_xlabel(r'Ionic Radius ($\AA$)')
ax1.set_ylabel(r'$D_i$')
ax1.set_ylim(0.005,3000)
ax1.legend()

# Levenberg-Marquardt algorithm
ax2 = fig.add_subplot(1,2,2)
ax2.set_title("Levenberg-Marquardt algorithm")
ax2.scatter(I_r, Di, s=80, color='#c7ddf4', edgecolors='k', label='4 GPa - 1073 K, Kessel et al., 2005')

popt2, pcov2 = curve_fit(func, I_r, Di, method='lm', p0=(1.1,100,100))

x2 = np.linspace(0.85,1.2,1000)
y2 = func(x2,popt2[0],popt2[1], popt2[2])
ax2.plot(x2,y2, color='#4881e9', linewidth=2, linestyle ='--', label=r'$r_0$ = ' + str(round(popt2[0],3)) + r', $D_0$ = ' + str(round(popt2[1],0)) + ', E = ' + str(round(popt2[2],0)))
add_elements(ax = ax2)
ax2.set_yscale('log')
ax2.set_xlabel(r'Ionic Radius ($\AA$)')
ax2.set_ylabel(r'$D_i$')
ax2.set_ylim(0.005,3000)
ax2.legend()

fig.tight_layout()