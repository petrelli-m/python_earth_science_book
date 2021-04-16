def pressure(r, ro, g):
    
    p = np.zeros(len(r))
    r = r *1000
    
    for i in range(0,len(r)):    
        r1 = r[i:len(r)]
        ro1 = ro[i:len(r)]
        g1 = g[i:len(r)]
        y = ro1*g1
        p1 = trapz(y,r1)
        p[i] = p1
    return p
    
p = pressure(r,ro,g)/1e9 # expressed in GPa
z = np.linspace(6400, 1, 6400)

fig, ax = plt.subplots()  
ax.plot(z,p)
ax.grid()
ax.set_ylabel('P [GPa]')
ax.set_xlabel('Depth z from the Earth Surface [km]')
