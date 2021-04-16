def numpy_ftcs(u, d, h, dt):

    d2u_dx2 = np.zeros(u.shape, np.float)
    d2u_dx2[1:-1] = (u[2:] - 2 * u[1:-1] + u[:-2]) / h**2

    # Neuman boundary conditions at i=0 and i=len(u)-1
    i = 0
    d2u_dx2[i] = (u[i+1] - 2 * u[i] + u[i]) / h**2
    i = len(u)-1
    d2u_dx2[i] = (u[i] - 2 * u[i] + u[i-1]) / h**2

    # Euler method for the time domain
    u1 = u + dt * D * d2u_dx2
    return u1
