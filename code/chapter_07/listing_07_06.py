import numpy as np
from scipy.integrate import trapz
import matplotlib.pyplot as plt

r = np.linspace(1,6400,6400)

def density():
    ro_inner_core = np.linspace(13100, 12800, 1220)
    ro_outer_core = np.linspace(12200, 9900, 2259)
    ro_lower_mantle = np.linspace(5600,4400,2171)
    ro_upper_mantle = np.linspace(4130,3400,720)
    ro_crust = np.linspace(3100,2700,30)
   
    ro_final = np.concatenate((ro_inner_core, ro_outer_core, ro_lower_mantle, ro_upper_mantle, ro_crust))
    
    return ro_final

ro = density()

fig, ax = plt.subplots()
ax.plot(r,ro, label="Densities on the Earth's Interior")
ax.set_ylabel(r"Density [Kg/m$^3$]")
ax.set_xlabel("Distance from the Earth center r [km]")
ax.legend()
ax.grid()
