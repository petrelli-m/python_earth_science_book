import pandas as pd
import matplotlib.pyplot as plt

my_dataset1 = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

x = my_dataset1.Zr
y = my_dataset1.Th

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax1.scatter(x, y, marker='s', color='#ff464a', edgecolor='#000000')
ax1.set_title("using scatter()")
ax1.set_xlabel("Zr [ppm]")
ax1.set_ylabel("Th [ppm]")
ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(x, y, marker='s', linestyle='', color='#ff464a', markeredgecolor='#000000')
ax2.set_title("using plot()")
ax2.set_xlabel("Zr [ppm]")
ax2.set_ylabel("Th [ppm]")
fig.tight_layout()
