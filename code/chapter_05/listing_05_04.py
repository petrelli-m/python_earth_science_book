import pandas as pd
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

my_range = my_dataset['Zr'].max()- my_dataset['Zr'].min()

print ('-------')
print ('Range')
print("{0:.0f}".format(my_range))
print ('-------')

fig, ax = plt.subplots()
ax.hist(my_dataset.Zr, bins=20, density=True, edgecolor='k', label='Measurements Hist') 
ax.axvline(my_dataset['Zr'].max(), color='purple', label='Max value', linewidth=2)
ax.axvline(my_dataset['Zr'].min(), color='green', label='Min value', linewidth=2)
ax.axvspan(my_dataset['Zr'].min(), my_dataset['Zr'].max(), alpha=0.1, color='orange', label='Range = ' + "{0:.0f}".format(my_range) + ' ppm')
ax.set_xlabel('Zr [ppm]')
ax.set_ylabel('Probability density')
ax.legend()

