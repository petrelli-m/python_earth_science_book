import pandas as pd
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

variance =  my_dataset['Zr'].var()
stddev =  my_dataset['Zr'].std()

print ('-------')
print ('Variance')
print("{0:.0f} [square ppm]".format(variance))
print ('-------')
print ('Standard Deviation')
print("{0:.0f} [ppm]".format(stddev))
print ('-------')

fig, ax = plt.subplots()
ax.hist(my_dataset.Zr, bins= 20, density = True, edgecolor='k', label='Measurements Hist') 
ax.axvline(my_dataset['Zr'].mean()-stddev, color='purple', label=r'mean - 1$\sigma$', linewidth=2)
ax.axvline(my_dataset['Zr'].mean()+stddev, color='green', label=r'mean + 1$\sigma$', linewidth=2)
ax.axvspan(my_dataset['Zr'].mean()-stddev, my_dataset['Zr'].mean()+stddev, alpha=0.1, color='orange', label=r'mean $\pm$ 1$\sigma$')
ax.set_xlabel('Zr [ppm]')
ax.set_ylabel('Probability density')
ax.legend()

'''
Output:
-------
Variance
14021 [square ppm]
-------
Standard Deviation
118 [ppm]
-------
'''