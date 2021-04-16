import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(-1, 1, 10) 
y = x

X, Y = np.meshgrid(x, y) 

dx_dt = np.ones_like(X)
dy_dt = - Y - 2 * X**2 

# Making plot 
fig = plt.figure() 
ax1 = fig.add_subplot(1, 2, 1)
ax1.quiver(X, Y, dx_dt, dy_dt) 
ax1.set_title('using quiver()')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.axis('square')

ax2 = fig.add_subplot(1, 2, 2)
ax2.streamplot(X, Y, dx_dt, dy_dt, linewidth=0.5)
ax2.set_title('using streamplot()')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.axis('square')

fig.tight_layout()
