def gravity(r):
    
    g = np.zeros(len(r))
    Gr = 6.67408e-11
    r = r * 1000 # from Km to m
    
    for i in range(1,len(r)):
        
        r1 = r[0:i]
        ro1  = ro[0:i]
        r2 = r1[i-1]
    
        y = ro1*r1**2
        y_int = trapz(y,r1)
        
        g1 = ((4 * np.pi*Gr)/(r2**2)) * y_int
        g[i] = g1
           
    return g

g = gravity(r)

fig, ax = plt.subplots()
ax.plot(r,g)
ax.grid()
ax.set_ylabel(r'g [m/s$^2]$')
ax.set_xlabel('Distance from the Earth center r [km]')
