import numpy as np
from scipy import integrate


x = np.linspace(0,9, 3) # 3 divisions %*\textcolor{codegreen}{$[x_0,x_1,x_2]$}*), n=2 
y = x**2

sup_trapz = integrate.trapz(y,x)
sup_simps = integrate.simps(y,x)


print('Using n=2, the trapezoidal rule returns a value of {:.0f}'.format(sup_trapz))
print('Using n=2, the composite Simpson rule returns a value of {:.0f}'.format(sup_simps))

'''
Output:
Using n=2, the trapezoidal rule returns a value of 273
Using n=2, the composite Simpson rule returns a value of 243
'''