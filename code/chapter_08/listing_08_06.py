import numpy as np
from scipy import special
import matplotlib.pyplot as plt

def plane_diff_1d(t, D, x0=0, xmin=-1, xmax=1, c_left=1, c_right=0, num_points=200):
    
     n = num_points
     x = np.linspace(xmin, xmax, n)
     delta_c = c_left - c_right
     
     c0 = np.piecewise(x, [x < x0, x >= x0], [c_left, c_right])
     c = 0.5 * delta_c * (special.erfc((x - x0)/(2 * np.sqrt(D * t))))
  
     return x, c, c0

D = 0.01 # Diffusion coefficient

fig, ax = plt.subplots()  

for t in range(1, 14, 3):

    x, c, c0 = plane_diff_1d(t=t, D=D)
    if t==1:
        leg = "t = " + str(t)
        plt.plot(x, c0, label="t = 0")
    leg = "t = " + str(t)    
    ax.plot(x, c, label=leg)
    
ax.grid()
ax.set_xlabel('x')
ax.set_ylabel('C')  
ax.legend()

