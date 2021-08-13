import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import ode

# using scipy.integrate.ode
def ode_sol(n0, decay_const, t_final, n_t_steps):
    intermediate_points = n_t_steps
    t3 = np.linspace(0,t_final, intermediate_points)
    n3 = np.zeros(t3.shape, float) 
    def f(t, y, decay_const):
        return  - decay_const * y 
    solver = ode(f).set_integrator('dopri5') # runge-kutta of order (4)5
    y0 = n0
    t0 = 0
    solver.set_initial_value(y0, t0)
    solver.set_f_params(decay_const)
    k=1
    n3[0] = n0
    while solver.successful() and solver.t < t_final:
        n3[k] = solver.integrate(t3[k])[0]
        k += 1  # k = k + 1
    n3r = n3 / n0
    return n3, n3r, t3

# Analytical solution
na, nar, ta = analytical_solution(n0=10000, decay_const=1.54e-1, t_final=20, n_t_steps=10)
# Euler method
ne, ner, te = euler_method(n0=10000, decay_const=1.54e-1, t_final=20, n_t_steps=10)
nuler_rel_error = 100*(ne-na)/na
# runge-kutta of order (4)5
n_ode, n_oder, tode = ode_sol(n0=10000, decay_const=1.54e-1, t_final=20, n_t_steps=10)
ode_rel_error = 100*(n_ode - na) / na

# Make the plot
fig = plt.figure(figsize=(8,5))
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(ta, nar, linestyle="-", linewidth=2, label='Analytical Solution', c='#ff464a')
ax1.plot(te, ner, linestyle="--", linewidth=2, label='Euler method', c='#4881e9')
ax1.plot(tode, n_oder, linestyle="--", linewidth=2, label='Runge-Kutta of order (4)5', c='#342a77')
ax1.set_ylabel('Relative Number of $^{238}$U atoms')
ax1.set_xlabel('Time in bilion years')  
ax1.legend()

ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(te, euler_rel_error, linestyle="-", linewidth=2, c='#4881e9', label='Euler method')
ax2.plot(tode, ode_rel_error, linestyle="-", linewidth=2, c='#342a77', label='Runge-Kutta of order (4)5')
ax2.set_ylabel('Relative Error, in %')
ax2.set_xlabel('Time in bilion years')  
ax2.legend()

fig.tight_layout()



