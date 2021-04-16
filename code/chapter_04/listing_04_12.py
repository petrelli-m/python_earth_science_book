# Explicit positive and negative reporting
a = +5.34352
b = -6.3421245
print('-------------------------------------------------')
print("The plus symbol is not reported: {:.2f} | {:.2f}".format(+5.34352, -6.3421245))
print("The plus symbol is reported: {:+.2f} | {:+.2f}".format(a, b))
print('-------------------------------------------------')

# Reporting as percent
c = 0.1558
print('-------------------------------------------------')
print("Reporting as percent: {:.1%}".format(c))
print('-------------------------------------------------')

# Scientific notation
d = 6580000000000
print('-------------------------------------------------')
print("Scientific notation using e: {:.1e}".format(d))
print("Scientific notation using E: {:.1E}".format(d))
print('-------------------------------------------------')

'''Results
-------------------------------------------------
The plus symbol is not reported: 5.34 | -6.34
The plus symbol is reported: +5.34 | -6.34
-------------------------------------------------
-------------------------------------------------
Reporting as percent: 15.6%
-------------------------------------------------
-------------------------------------------------
Scientific notation using e: 6.6e+12
Scientific notation using E: 6.6E+12
-------------------------------------------------
'''




