from statsmodels.nonparametric.kde import KDEUnivariate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

x = my_dataset.Zr
x_eval = np.arange(0, 1100, 1)

fig = plt.figure()

ax1 = fig.add_subplot(2, 1, 1)
# Density Histogram
ax1.hist(x, bins='auto', density=True, label='Density Histogram', color='#c7ddf4', edgecolor='#000000') 
kde = KDEUnivariate(x)
kde.fit()
my_kde = kde.evaluate(x_eval)
ax1.plot(x_eval, my_kde, linewidth=1.5, color='#ff464a', label='gaussian KDE - auto bandwidth selection')
ax1.set_xlabel('Zr [ppm]')
ax1.set_ylabel('Probability density')
ax1.legend()

ax2 = fig.add_subplot(2, 1, 2)
# Density Histogram
ax2.hist(x, bins= "auto", density = True, label='Density Histogram', color='#c7ddf4', edgecolor='#000000') 

# KDE
# Effect of bandwidth 
for my_bw in [10,50,100]:

    kde = KDEUnivariate(x)
    kde.fit(bw = my_bw)
    
    my_kde = kde.evaluate(x_eval)
    ax2.plot(x_eval, my_kde, linewidth = 1.5, label='gaussian KDE - bw: ' + str(my_bw))
    
ax2.set_xlabel('Zr [ppm]')
ax2.set_ylabel('Probability density')
ax2.legend()

fig.tight_layout()