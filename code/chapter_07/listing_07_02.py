import numpy as np

def integrate_trap(f, a, b, n):
    # Implementation of the trapezoidal rule
    h = (b-a)/n
    x = np.linspace(a, b, n+1) 
    i=1
    area = h*(f(x[0]) + f(x[n]))/2
    while i<n:
        sup_rect = f(x[i])*h
        area += sup_rect 
        i += 1 
    return area

'''
We test the trapezoidal rule on the known sine funcion were the  
definite integral in the interval [0, %*\textcolor{codeviolet}{$\pi$}*)/2] is equal to 1. 
'''

sup_5 = integrate_trap(np.sin, 0, np.pi/2, 5)
sup_10 = integrate_trap(np.sin, 0, np.pi/2, 10)

print('Using n=5, the trapezoidal rule returns a value of {:.2f}'.format(sup_5))
print('Using n=10, the trapezoidal rule returns a value of {:.2f}'.format(sup_10))
   
'''
Output:
Using n=5, the trapezoidal rule returns a value of 0.99
Using n=10, the trapezoidal rule returns a value of 1.00
'''
 
