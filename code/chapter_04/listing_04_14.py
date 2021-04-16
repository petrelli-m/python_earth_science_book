import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def my_line(x, m, q):
    y = m * x + q
    return y


my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_majors', engine='openpyxl')

my_dataset1 = my_dataset[my_dataset.Epoch == 'one']
my_dataset2 = my_dataset[my_dataset.Epoch == 'two']

x = np.linspace(52.5, 62, 100)
y = my_line(x, m=0.3, q=-10.3)

fig, ax = plt.subplots()

ax.scatter(my_dataset1.SIO2, my_dataset1.K2O, marker='s', color='#c7ddf4', edgecolor='#000000', label=r'$1^{st}$ Epoch')
ax.scatter(my_dataset2.SIO2, my_dataset2.K2O, marker='s', color='#ff464a', edgecolor='#000000', label=r'$2^{nd}$ Epoch')
ax.plot(x, y, color='#342a77')

ax.annotate(r'What is the 1$\sigma$ for this point?', xy=(47.6, 6.6), xytext=(47, 8.8), arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
ax.text(52.4, 5.6, r'$ Na_2O = 0.3 \cdot SiO_2 -10.3$', dict(size=10, rotation=33))

ax.text(53.5, 5.1, r'$ \mu_{SiO_2} = \frac {a_{1}+a_{2}+\cdots +a_{n}}{n}$ = ' + '{:.1f} [wt.%]'.format(57.721),  dict(size=11.5))

ax.set_xlabel(r'SiO$_2$ [wt%]')
ax.set_ylabel(r'K$_2$O [wt%]')

ax.legend()
