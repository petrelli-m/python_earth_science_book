import matplotlib.pyplot as plt
import numpy as np

def ec(f, d, c0):
    cl = c0/(d * (1-f) + f)
    return cl

my_f = np.linspace(0.3, 1, 8)

my_c = ec(f=my_f, d=0.1, c0=100)

fig, ax = plt.subplots() 
ax.plot(my_f, my_c, label="Eq cryst. D = 0.1")

ax.set_xlabel('F')
ax.set_ylabel('C [ppm]')
ax.legend()
