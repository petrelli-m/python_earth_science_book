def ec(f, d, c0):
    cl = c0/(d * (1-f) + f)
    return cl

my_c = ec(f=0.5, d=0.1, c0=100)

print('RESULT: '+ str(int(my_c)) + ' ppm')

''' 
Output:
RESULT: 181 ppm
'''