import numpy as np
from matplotlib import pyplot as plt

# Direction Field
def direction_field(x_min, x_max, y_min, y_max, n_step, lenght, fun, ax):
   
    # this is to avoid RuntimeWarning: divide by zero
    np.seterr(divide='ignore', invalid='ignore') 
    
    x = np.linspace(x_min, x_max, n_step)
    y = np.linspace(y_min, y_max, n_step)
    X, Y = np.meshgrid(x, y) 
    slope = fun(X,Y)
    slope = np.where(slope == np.inf, 10**3, slope) 
    slope = np.where(slope == -np.inf, -10**3, slope)
    delta = lenght * np.cos(np.arctan(slope))
    X1 = X - delta 
    X2 = X + delta 
    Y1 = slope*(X1-X)+Y
    Y2 = slope*(X2-X)+Y
    ax.plot([X1.ravel(), X2.ravel()], [Y1.ravel(), Y2.ravel()], 'k-', linewidth=1)

# Differential equations
def my_ode(x, y):
    dy_dx =  x**2 / (1 - x**2 - y**2)
    return dy_dx 

# Make the plot
fig, ax1 = plt.subplots()  
direction_field(x_min=-2, x_max=2, y_min=-2, y_max=2, n_step=30, lenght=0.05, fun=my_ode, ax=ax1)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.axis('square')
ax1.set_title(r"$ {y}' = - \frac{x^2}{1 - x^2 - y^2} $")     
