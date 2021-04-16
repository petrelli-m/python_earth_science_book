import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name=1)
el = 'Pb'
my_sub_dataset = my_dataset[my_dataset.Epoch == 'three-b']
my_sub_dataset = my_sub_dataset.dropna(subset=[el])
a_mean = my_sub_dataset[el].mean()
median = my_sub_dataset[el].median()
range_values = [my_sub_dataset[el].min(), my_sub_dataset[el].max()]
std_dev_values =  [a_mean - my_sub_dataset[el].std(), a_mean + my_sub_dataset[el].std()]
IQR_values = [np.percentile(my_sub_dataset[el], 25, interpolation = 'midpoint'), np.percentile(my_sub_dataset[el], 75, interpolation = 'midpoint')]                                                                                        
MADn_values = [median - stats.median_abs_deviation(my_sub_dataset[el], scale='normal'), median + stats.median_abs_deviation(my_sub_dataset[el], scale='normal')]

scales_values = [range_values, std_dev_values, IQR_values, MADn_values]
scale_labels = ['Range', 'Standard Deviation', 'Inter Quartile Range', 'Median Absolute Deviation']
locations = [a_mean, a_mean, median, median]
location_labels = ['Arithmetic Mean', 'Arithmetic Mean', 'Median', 'Median']
binnings = ['auto', np.arange(0,300,5),np.arange(50,150,5),np.arange(50,150,5)]
indexes = [1,2,3,4]

fig = plt.figure(figsize=(8,6))
for scale_values, location, scale_label, location_label, bins, index in zip(scales_values, locations, scale_labels, location_labels, binnings, indexes):
    ax = fig.add_subplot(2, 2, index)
    ax.hist(my_sub_dataset[el], density=True, edgecolor='k', color='#4881e9', bins=bins)
    ax.axvline(location, color='#ff464a', linewidth=1, label=location_label)
    ax.axvline(scale_values[0], color='#ebb60d')
    ax.axvline(scale_values[1], color='#ebb60d')
    ax.axvspan(scale_values[0], scale_values[1], alpha=0.1, color='orange', label=scale_label)
    ax.set_xlabel(el + " [ppm]")
    ax.set_ylabel('probability density')
    ax.set_ylim(0, 0.1)
    ax.legend(loc = 'upper right')
fig.tight_layout()
 
    