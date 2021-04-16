import numpy as np

def integrate_rec(f, a, b, n):
    # Implementation of the rectanlge method 
    h = (b-a)/n
    x = np.linspace(a, b, n+1) 
    i=0
    area=0
    while i<n:
        sup_rect =  f(x[i])*h
        area += sup_rect
        i += 1 
    return area
'''
We test the Rectangle method on the sine funcion were the definite integral in the interval [0, %*\textcolor{codeviolet}{$\pi$}*)/2] is equal to 1. 
'''

sup_5 = integrate_rec(np.sin, 0, np.pi/2, 5)
sup_10 = integrate_rec(np.sin, 0, np.pi/2, 10)
sup_100 = integrate_rec(np.sin, 0, np.pi/2, 100)

print('Using n=5, the rectangle method returns a value of {:.2f}'.format(sup_5))
print('Using n=10, the rectangle method returns a value of {:.2f}'.format(sup_10))
print('Using n=100, the rectangle method returns a value of {:.2f}'.format(sup_100))
     
'''
Output:
Using n=5, the rectangle method returns a value of 0.83
Using n=10, the rectangle method returns a value of 0.92
Using n=100, the rectangle method returns a value of 0.99
'''
 
