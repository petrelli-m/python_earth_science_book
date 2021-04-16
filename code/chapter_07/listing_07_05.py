def simple_lithopress(z,ro=2900, g=9.8):
    pressure = z*g*ro/1e6 # return the pressure in MPa
    return pressure

my_pressure = simple_lithopress(z=2000)
print('The pressure at 2000 meters is {0:.0f} MPa'.format(my_pressure))

'''
Output: The pressure at 2000 meters is 57 MPa
'''
