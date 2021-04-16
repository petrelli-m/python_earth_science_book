import numpy as np # import numpy

# relevant constants
GREEK_P = np.pi 
EULER_NUMBER = np.e

# print greek_p and euler_number on the screen
print("Archimedes' constant is " + str(GREEK_P))
print("Euler's number is " + str(EULER_NUMBER))

# trigonometric functions
x = np.sin(GREEK_P / 2) # x = 1 expected

# print the result on the screen
print("The sine of a quarter of radiant is " + str(x))


# defining a 1D array in numpy
my_array = np.array([4, 8, 27]) 
# print myArray on the screen
print("myArray is equal to " + str(my_array))

log10_my_array = np.log10(my_array)

# print the result on the screen
print("The base-10 logarithms of the elements in myArray are")
print(log10_my_array)

'''
Output:
Archimedes' constant is 3.141592653589793
Euler's number is 2.718281828459045
The sine of a quarter of radiant is 1.0
myArray is equal to [ 4  8 27]
The base-10 logarithms of the elements in myArray are
[0.60205999 0.90308999 1.43136376]
'''
