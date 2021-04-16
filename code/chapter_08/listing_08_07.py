def ftcs(u, D, h, dt):
    
    d2u_dx2 = np.zeros(u.shape, np.float) 
    for i in range(1,len(u)-1):
        # Central difference scheme in space
        d2u_dx2[i] = (u[i+1] - 2*u[i] + u[i-1]) / h**2
        
    # Neuman boundary conditions at i=0 and i=len(u)-1
    i=0
    d2u_dx2[i] = (u[i+1] - 2 * u[i] + u[i]) / h**2
    i=len(u)-1
    d2u_dx2[i] = (u[i] - 2 * u[i] + u[i-1]) / h**2
    
    # Euler method for the time domain
    u1 = u + dt * D * d2u_dx2
    return u1
    
dt = 0.001  #step size of time
tf = 3

def compute_d_const(u, d, h, dt, tf):
    
    nsteps = tf/dt
    u1 = u
    for i in range(int(nsteps)):
        u1 =  ftcs(u1, D, h, dt)
    return u1

x, c, c0 = plane_diff_1d(t=tf, D=D)

h = x[1] - x[0] #step size of the 1D space
u = c0 # intial conditions
c1 = compute_d_const(u, D, h, dt, tf)

fig, ax = plt.subplots()  
ax.plot(x,c0, label='initial conditions')
ax.plot(x,c,'y', label='analytical solution')
ax.plot(x,c1,'r--', label='numerical solution') 
ax.set_xlabel('x')
ax.set_ylabel('C')   
ax.legend()
