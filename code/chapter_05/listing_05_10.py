import pandas as pd
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

fig, ax = plt.subplots()
my_flierprops = dict(markerfacecolor='#f8e9a1', markeredgecolor='#24305e', marker='o')
my_medianprops = dict(color='#f76c6c', linewidth = 2)
my_boxprops = dict(facecolor='#a8d0e6', edgecolor='#24305e')
ax.boxplot(my_dataset.Zr, patch_artist = True, notch=True, flierprops=my_flierprops, medianprops=my_medianprops, boxprops=my_boxprops) 
ax.set_ylabel('Zr [ppm]')
ax.set_xticks([1])
ax.set_xticklabels(['all Epochs'])
plt.show()