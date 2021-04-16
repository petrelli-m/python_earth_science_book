import numpy as np
from scipy.stats import skew

a_mean = my_dataset.Zr.mean()
median = my_dataset.Zr.median()
hist, bin_edges = np.histogram(my_dataset['Zr'], bins=20, density=True)
modal_value = (bin_edges[hist.argmax()] + bin_edges[hist.argmax()+1])/2
standard_deviation = my_dataset['Zr'].std()

a1 = (a_mean - modal_value) / standard_deviation 
a2 = 3 * (a_mean - median) / standard_deviation
g1 = skew(my_dataset['Zr'])

print ('-------')
print ("Pearson's first coefficient of skewness: {:.2f}".format(a1))
print ("Pearson's 2nd moment of skewness: {:.2f}".format(a2))
print ("Fisher-Pearson's coefficient of skewness: {:.2f}".format(g1))
print ('-------')

'''
Output:
-------
Pearson's first coefficient of skewness: 0.74
Pearson's 2nd moment of skewness: 0.66
Fisher-Pearson's coefficient of skewness: 1.26
-------
'''