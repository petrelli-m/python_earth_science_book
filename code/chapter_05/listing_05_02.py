import pandas as pd
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

median = my_dataset.Zr.median()

print ('-------')
print ('median')
print("{0:.1f} [ppm]".format(median))
print ('-------')

fig, ax = plt.subplots()
ax.hist(my_dataset.Zr, bins=20, density=True, edgecolor='k', label="Measurements Hist", alpha=0.8) 
ax.axvline(median, color='orange', label='Median', linewidth=2)
ax.set_xlabel('Zr [ppm]')
ax.set_ylabel('Probability density')
ax.legend()

'''
Output:
-------
median
339.4 [ppm]
-------
'''