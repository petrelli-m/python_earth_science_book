import pandas as pd
import matplotlib.pyplot as plt

my_dataset1 = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

x = my_dataset1.Zr
y = my_dataset1.Th
dx = my_dataset1.Zr * 0.1
dy = my_dataset1.Th * 0.1

fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=dx, yerr=dy, marker='o', markersize=4, linestyle='', color='#c7ddf4', markeredgecolor='k', ecolor='0.7', label='Recent CFC activity')
ax.set_xlabel('Zr [ppm]')
ax.set_ylabel('Th [ppm]')
ax.legend(loc='upper left')

