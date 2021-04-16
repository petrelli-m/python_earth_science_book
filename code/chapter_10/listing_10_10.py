import sympy as sym

a, b, sigma_a, sigma_b = sym.symbols("a b sigma_a sigma_b")

def symbolic_error_prop(func, val_a, val_sigma_a, val_b=0, val_sigma_b=0):
    
    z = sym.lambdify([a,b],func, 'numpy')
    sigma_z = sym.lambdify([a, b, sigma_a, sigma_b], sym.sqrt((sym.diff(func, a)**2 * sigma_a**2)+(sym.diff(func, b)**2 * sigma_b**2)), 'numpy')
    val_z = z(a=val_a, b=val_b)
    val_sigma_z = sigma_z(a=val_a, b=val_b, sigma_a=val_sigma_a, sigma_b=val_sigma_b)
    
    return val_z, val_sigma_z