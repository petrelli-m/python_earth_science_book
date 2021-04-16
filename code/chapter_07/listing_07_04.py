import numpy as np
from scipy import integrate

conturs_areas = np.array([194135, 136366, 79745, 38335, 18450, 9635, 3895])
x = np.array([0,25,50,75,100,125,150])

vol_traps = integrate.trapz(conturs_areas, x)
vol_simps = integrate.simps(conturs_areas, x)

print('The trapezoidal rule returns a volume of {:.0f} cubic meters'.format(vol_traps))
print('The composite Simpson rule returns a volume of {:.0f} cubic meters'.format(vol_simps))

'''
Output:
The trapezoidal rule returns a volume of 9538650 cubic meters
The composite Simpson rule returns a volume of 9431367 cubic meters   
'''