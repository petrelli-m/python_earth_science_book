import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Model parameters
T = 1200.0 # Temperature in Celsius
dx = 4.12 # average distance in micron among the analyses
dt = 0.9 * 1e4
RT = 8.3144 * (T + 273.15)
R = dt / dx ** 2

# Initial Conditions
my_dataset = pd.read_excel('Moore_Phd.xlsx')
my_distance = my_dataset.Distance.values
Mg_C = my_dataset.MgO.values
An = my_dataset.An_mol_percent.values
An = An / 100
An_unsmoothed = An
An_smoothed = np.full(len(An),0.)

# Smooting the An profile to avoid numerical artifacts
D_smoot = np.full(len(An),0.0005)
for i in range(2):
    An_smoothed[1:-1] =  An_unsmoothed[1:-1] + R * D_smoot[1:-1] * (An_unsmoothed[2:] - 2 * An_unsmoothed[1:-1] + An_unsmoothed[:-2])
    An_smoothed[0] = An[0]
    An_smoothed[len(An)-1] = An[len(An)-1]
    an_unsmoothed = An_smoothed

D_Mg = 2.92 * 10**(-4.1 * An_smoothed - 3.1)*np.exp(-266 * 1e3/RT)*1e12  # Eq. 8 in Costa et al., 2003
  
fig, ax = plt.subplots(figsize=(7,5))
  
# Initial and Equilibrium Profiles
A = - 21882
B = - 26352
K = np.exp((A*An_smoothed+B)/RT) # Eq. 8 in Moore et al., 2014
c_eq = 8.4 * K
c_init = 7.8 * K
ax.plot(my_distance, c_eq, linewidth=2, color='#ff464a', label ='Equilibrium Profile')
ax.plot(my_distance, c_init,linewidth=2,  color='#342a77', label='Initial Profile')

# The numerical solution start here
colors = ['#4881e9','#e99648','#e9486e']
t_final_weeks = np.array([4,10,21])

for t_w, color in zip(t_final_weeks,colors):

    C_Mg_new = np.full(len(c_eq),0.)
    d2An = np.full(len(c_eq),0.)
    d2C_Mg = np.full(len(c_eq),0.)
    dD_Mg = np.full(len(c_eq),0.)
    dC_Mg = np.full(len(c_eq),0.)
    dAn = np.full(len(c_eq),0.)
    
    C_Mg = c_init
    t_final = int(604800 * t_w/dt)
    for i in range(t_final):
        # boundary conditions: Rims are at equilibrium with melt
        C_Mg_new[0] = c_eq[0]
        C_Mg_new[len(c_eq)-1] = c_eq[len(c_eq)-1]
        
        # Finite difference sol. of Eq. 7 in Costa et al., 2003
        d2An[1:-1] = (An_smoothed[2:] - 2 * An_smoothed[1:-1] + An_smoothed[:-2])
        d2C_Mg[1:-1] = C_Mg[2:] - 2 * C_Mg[1:-1] + C_Mg[:-2]
        dD_Mg[1:-1] =  (D_Mg[2:]-D_Mg[:-2])/2
        dC_Mg[1:-1] = (C_Mg[2:]-C_Mg[:-2])/2
        dAn[1:-1] =  (An_smoothed[2:]-An_smoothed[:-2])/2
        
        C_Mg_new[1:-1] = C_Mg[1:-1] + R * ( (D_Mg[1:-1] * d2C_Mg[1:-1] + dD_Mg[1:-1] * dC_Mg[1:-1]) - (A/RT) * (D_Mg[1:-1] * dC_Mg[1:-1] * dAn[1:-1]  +  C_Mg[1:-1] * dD_Mg[1:-1] * dAn[1:-1] + D_Mg[1:-1] * C_Mg[1:-1] * d2An[1:-1]) )
        C_Mg = C_Mg_new
    ax.plot(my_distance, C_Mg_new, linestyle='--', linewidth=1, label= str(t_w) + ' weeks at 1200 Celsius deg.')
    
ax.scatter(my_distance, Mg_C, marker='o', c='#c7ddf4', edgecolors= 'k', s=50, label='Analytical Deteminations', zorder=100, alpha=0.7) 
ax.set_ylim(0.19,0.27)
 
time_sec = t_final * dt
time_weeks = time_sec / 604800
ax.legend(title=r'$\bf{4202\_1-Pl1}$ (Moore et al., 2014)', ncol=2, loc='lower center')
ax.set_xlabel(r'Distance [$\mu m$]')
ax.set_ylabel('MgO  [wt %]')
fig.tight_layout()


















