import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

q1 = np.percentile(my_dataset.Zr, 25, interpolation = 'midpoint') 
q3 = np.percentile(my_dataset.Zr, 75, interpolation = 'midpoint') 
  
iqr = q3 - q1 # Interquaritle range (IQR)  

print ('-------')
print ('Interquaritle range (IQR): {0:.0f} [ppm]'.format(iqr))
print ('-------')

fig, ax = plt.subplots()
ax.hist(my_dataset.Zr, bins='auto', density=True, edgecolor='k', label='Measurements Hist') 
ax.axvline(q1, color='purple', label='Q1', linewidth=2)
ax.axvline(q3, color='green', label='Q3', linewidth=2)
ax.axvspan(q1, q3, alpha=0.1, color='orange', label='Interquaritle range (IQR)')
ax.set_xlabel('Zr [ppm]')
ax.set_ylabel('Probability density')
ax.legend()

'''
Output:
-------
Interquaritle range (IQR): 164 [ppm]
-------
'''