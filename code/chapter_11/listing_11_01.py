import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

my_dataset_majors = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_majors')
my_dataset_traces = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

fig = plt.figure()

# MnO
MnO = my_dataset_majors.MNO

ax1 = fig.add_subplot(2, 1, 1)
ax1.hist(MnO, bins='auto', density=True, color='#4881e9', edgecolor='k', label='MnO', alpha=0.8) 
a_mean = MnO.mean()
std_dev = MnO.std()
x = np.linspace(a_mean-4*std_dev, a_mean+4*std_dev,1000)
pdf = norm.pdf(x, loc=a_mean, scale=std_dev)
ax1.plot(x, pdf, linewidth=1.5, color='#ff464a',label='Normal PDF')
ax1.set_xlabel('MnO [wt %]')
ax1.set_ylabel('Probability density')
ax1.legend()

#Pb
Pb = my_dataset_traces.Pb
Pb = Pb.dropna(how='any')
ax2 = fig.add_subplot(2, 1, 2)
ax2.hist(Pb, bins='auto', density=True, color='#4881e9', edgecolor='k', label='Pb', alpha=0.8) 
a_mean = Pb.mean()
std_dev = Pb.std()
x = np.linspace(a_mean-4*std_dev, a_mean+4*std_dev,1000)
pdf = norm.pdf(x, loc=a_mean, scale=std_dev)
ax2.plot(x, pdf, linewidth=1.5, color='#ff464a', label='Normal PDF')
ax2.set_xlabel('Pb [ppm]')
ax2.set_ylabel('Probability density')
ax2.legend()

fig.align_ylabels()
fig.tight_layout()