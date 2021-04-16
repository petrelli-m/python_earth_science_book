import matplotlib.pyplot as plt
import numpy as np

def ec(f, d, c0):
    cl = c0/(d * (1-f) + f)
    return cl

my_f = np.linspace(0.3,1, 8)

d = [0.1, 1, 2]

fig, ax = plt.subplots() 

for my_d in d:
    my_c = ec(f=my_f, d=my_d, c0=100)
    ax.plot(my_f, my_c, label='Eq cryst. D = ' +  str(my_d))


ax.set_xlabel('F')
ax.set_ylabel('C [ppm]')
ax.legend()
