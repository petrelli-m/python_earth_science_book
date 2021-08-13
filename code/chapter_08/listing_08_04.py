import matplotlib.pyplot as plt
import numpy as np

# Euler Method
def euler_method(n0, decay_const, t_final, n_t_steps):
    iterations = n_t_steps
    delta_t = t_final/n_t_steps
    t1 = np.linspace(0, iterations*delta_t, iterations)
    n1 = np.zeros(t1.shape, float) 
    n1[0]=n0
    for i in range(0,len(t1)-1):
        n1[i+1] = n1[i] * (1 - decay_const * delta_t )
    n1r = n1/n0
    return n1, n1r, t1

ne, ner, te = euler_method(n0=10000, decay_const=1.54e-1, t_final=20, n_t_steps=10)

#Analitical solution ...in the same points of the Euler method 
def analytical_solution(n0, decay_const, t_final, n_t_steps):
    
    intermediate_points = n_t_steps
    delta_t = t_final/n_t_steps
    t2 = np.linspace(0, intermediate_points*delta_t, intermediate_points)
    n2 = n0 * np.exp(-decay_const * t2 )
    n2r = n2/n0
    return n2, n2r, t2

na, nar, ta = analytical_solution(n0=10000, decay_const=1.54e-1, t_final=20, n_t_steps=10)

euler_rel_error = 100*(ne-na)/na

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(te, ner, linestyle="-", linewidth=2, label='Euler method')
ax1.plot(ta, nar, linestyle="--", linewidth=2, label='Analytical Solution')
ax1.set_ylabel('Relative Number of $^{238}$U atoms')
ax1.set_xlabel('time in bilion years')  
ax1.legend()

ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(te, euler_rel_error, linestyle="-", linewidth=2, label='Deviation formthe \nexpected value')
ax2.set_ylabel('Relative Error, in %')
ax2.set_xlabel('time in bilion years')  
ax2.legend()
