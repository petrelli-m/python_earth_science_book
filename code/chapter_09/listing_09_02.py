from scipy.stats import norm
import numpy as np
from scipy import special
from scipy import integrate

def integrate_normal(x1, x2, mu, sigma):
    sup = 0.5*((special.erf((x2-mu)/(sigma*np.sqrt(2))))-(special.erf((x1-mu)/(sigma*np.sqrt(2)))))
    return sup
    
my_mu = 0
my_sigma = 1

my_x1 = 0
my_x2 =  my_sigma

# The expected value is equal to 0.3413...
my_sup = integrate_normal(x1= my_x1, x2= my_x2, mu = my_mu, sigma = my_sigma)

x = np.arange(my_x1, my_x2, 0.0001)
y =  norm.pdf(x, loc=my_mu, scale= my_sigma) # normal_pdf(x, mean = my_mu, std = my_sigma)

sup_trapz = integrate.trapz(y,x)
sup_simps = integrate.simps(y,x)

print("Solution Using erf: {:.9f}".format(my_sup))
print("Using the trapezoidal rule, trapz: {:.10f}".format(sup_trapz))
print("Using the composite Simpson rule, simps: {:.10f}".format(sup_simps))

'''
Output:
Solution Using erf: 0.341344746
Using the trapezoidal rule, trapz: 0.3413205476
Using the composite Simpson rule, simps: 0.3413205478
'''