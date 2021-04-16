import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

a_mean = my_dataset.Zr.mean()

median = my_dataset.Zr.median()

hist, bin_edges = np.histogram(my_dataset['Zr'], bins=20, density=True)
modal_value = (bin_edges[hist.argmax()] +  bin_edges[hist.argmax()+1])/2

fig, ax = plt.subplots()
ax.hist(my_dataset.Zr, bins=20, density=True, edgecolor='k', label="Measurements Hist") 
ax.axvline(modal_value, color='orange', label='Modal Value', linewidth=2)
ax.axvline(median, color='purple',  label='Median Value', linewidth=2)
ax.axvline(a_mean, color='green',  label='Arithmetic mean', linewidth=2)
ax.set_xlabel('Zr [ppm]')
ax.set_ylabel('Probability density')
ax.legend()

