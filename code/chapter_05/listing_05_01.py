import pandas as pd
from scipy.stats.mstats import gmean, hmean
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

a_mean = my_dataset.Zr.mean()
g_mean = gmean(my_dataset['Zr'])
h_mean = hmean(my_dataset['Zr'])

print ('-------')
print ('arithmetic mean')
print ("{0:.1f} [ppm]".format(a_mean))
print ('-------')

print ('geometric mean')
print ("{0:.1f} [ppm]".format(g_mean))
print ('-------')

print ('harmonic mean')
print ("{0:.1f} [ppm]".format(h_mean))
print ('-------')

fig, ax = plt.subplots()
ax.hist(my_dataset.Zr, bins='auto', density=True, edgecolor='k', label='Measurements Hist', alpha=0.8) 
ax.axvline(a_mean, color='purple', label='Arithmetic mean', linewidth=2)
ax.axvline(g_mean, color='orange',  label='Geometric mean', linewidth=2)
ax.axvline(h_mean, color='green',  label='Harmonic mean', linewidth=2)
ax.set_xlabel('Zr [ppm]')
ax.set_ylabel('Probability density')
ax.legend()

'''
Output:
-------
arithmetic mean
365.4 [ppm]
-------
geometric mean
348.6 [ppm]
-------
harmonic mean
333.8 [ppm]
-------
'''