import pandas as pd
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax1.scatter(my_dataset.La, my_dataset.Ce, marker='o', edgecolor='k', color='#c7ddf4', label='CFC recent Activity')
ax1.set_xlabel('La [ppm]')
ax1.set_ylabel('Ce [ppm]')
ax1.legend()

ax2 = fig.add_subplot(2,1,2)
ax2.scatter(my_dataset.Sc, my_dataset.U, marker='o', edgecolor='k', color='#c7ddf4', label='CFC recent Activity')
ax2.set_xlabel('Sc [ppm]')
ax2.set_ylabel('U [ppm]')
ax2.legend()

