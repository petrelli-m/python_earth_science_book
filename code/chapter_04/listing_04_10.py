import pandas as pd
import matplotlib.pyplot as plt

my_dataset = pd.read_excel(
    'Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

my_dataset1 = my_dataset[my_dataset.Epoch == 'one']
my_dataset2 = my_dataset[my_dataset.Epoch == 'two']

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax1.scatter(my_dataset1.Zr, my_dataset1.Th, marker='s', color='#c7ddf4', edgecolor='#000000', label="First Epoch")
ax1.scatter(my_dataset2.Zr, my_dataset2.Th,  marker='o', color='#ff464a', edgecolor='#000000', label="Second Epoch")
ax1.set_xlabel("Zr [ppm]")
ax1.set_ylabel("Th [ppm]")
ax1.legend(loc='upper left', framealpha=1, frameon=True, title="Age < 15 ky", title_fontsize=10)

ax2 = fig.add_subplot(2, 1, 2)
ax2.scatter(my_dataset1.Zr, my_dataset1.Th, marker='s', color='#c7ddf4', edgecolor='#000000', label="First Epoch")
ax2.scatter(my_dataset2.Zr, my_dataset2.Th,  marker='o', color='#ff464a', edgecolor='#000000', label="Second Epoch")
ax2.set_xlabel("Zr [ppm]")
ax2.set_ylabel("Th [ppm]")
ax2.legend(frameon=False, loc='lower right', ncol=2, title="Age < 15 ky", title_fontsize=10)

fig.tight_layout()
