import pandas as pd
import matplotlib.pyplot as plt


def plot_errorbar(x,y, dx, dy, xoffset, yoffset, text, ax):
    ax.errorbar(x,y, xerr=dx, yerr=dy, marker='', linestyle = '', elinewidth = .5, capthick=0.5,  ecolor='k', capsize=3)
    ax.text(x + xoffset, y + yoffset, text)

my_dataset1 = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

x = my_dataset1.Zr
y = my_dataset1.Th

dx = 60
dy = 7

errorbar_x = x.max() - x.max() * 0.1
errorbar_y = y.min() + y.max() * 0.1

fig, ax1 = plt.subplots()
ax1.scatter(x, y, marker='o', color='#4881e9', edgecolor='k', alpha=0.8, label='Recent activity of the CFC')

plot_errorbar(errorbar_x, errorbar_y, dx, dy, dx/4, dy/4, r'2$\sigma$', ax1)

ax1.legend(loc='upper left')
ax1.set_xlabel('Zr [ppm]')
ax1.set_ylabel('Th [ppm]')
