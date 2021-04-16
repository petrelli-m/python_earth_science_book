import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

hist, bin_edges = np.histogram(my_dataset['Zr'], bins= 20, density=True)
modal_value = (bin_edges[hist.argmax()] +  bin_edges[hist.argmax()+1])/2

print ('modal value: {0:.0f} [ppm]'.format(modal_value))

fig, ax = plt.subplots()
ax.hist(my_dataset.Zr, bins=20, density=True, edgecolor='k', label="Measurements Hist", alpha=0.8) 
ax.axvline(modal_value, color="orange", label="Modal value", linewidth=2)
ax.set_xlabel('Zr [ppm]')
ax.set_ylabel('Probability density')
ax.legend()

'''
Output: modal value: 277 [ppm]
'''
