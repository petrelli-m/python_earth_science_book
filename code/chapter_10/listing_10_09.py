import numpy as np

def sum_ab(a, b, sigma_a, sigma_b):
    z = a + b
    sigma_z = np.sqrt(sigma_a**2 + sigma_b**2)
    return z, sigma_z

def division_ab(a, b, sigma_a, sigma_b):
    z = a / b
    sigma_z = z * np.sqrt((sigma_a/a)**2 + (sigma_b/b)**2)
    return z, sigma_z
