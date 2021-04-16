import pandas as pd
import numpy as np
from scipy.stats.mstats import winsorize
from scipy.stats import trim_mean
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name=1)

el = 'Pb' 
my_sub_dataset = my_dataset[my_dataset.Epoch == 'three-b']
my_sub_dataset = my_sub_dataset.dropna(subset=[el])
   
fig, ax = plt.subplots() 
a_mean = my_sub_dataset[el].mean()
median = my_sub_dataset[el].median()
trimmed_mean = trim_mean(my_sub_dataset[el], proportiontocut=0.1)
winsorized_mean = np.mean(winsorize(my_sub_dataset[el], limits=0.1))

delta = 100 * (a_mean-median) / median

bins = np.arange(50,240,5)
ax.hist(my_sub_dataset[el], density=True, edgecolor='k',  color='#4881e9', bins=bins, label = 'Lead (Pb), Epoch Three')
ax.axvline(a_mean, color='#ff464a', linewidth=2, label='Arithmetic Mean: {:.0f} [ppm]'.format(a_mean))
ax.axvline(median, color='#ebb60d', linewidth=2, label='Median: {:.0f} [ppm]'.format(median))
ax.axvline(trimmed_mean, color='#8f10b3', linewidth=2, label=r'Trimmed Mean ($\alpha = 0.1$):' + '{:.0f} [ppm]'.format(trimmed_mean))
ax.axvline(winsorized_mean, color='#07851e', linewidth=2, label=r'Winsored Mean ($\alpha = 0.1$):' + '{:.0f} [ppm]'.format(winsorized_mean))

ax.set_xlabel(el + " [ppm]")
ax.set_ylabel('probability density')
ax.legend()
ax.annotate('Large oulier at about 800 ppm', (240, 0.02), (220, 0.02), ha="right", va="center", size=9, arrowprops=dict(arrowstyle='fancy'))
ax.annotate('Deviation of the arithmetic\nmean from the median: {:.1f} %'.format(delta), (a_mean + 3, 0.03), (a_mean + 25, 0.03), ha="left", va="center", size=9, arrowprops=dict(arrowstyle='fancy'))
    
    
    