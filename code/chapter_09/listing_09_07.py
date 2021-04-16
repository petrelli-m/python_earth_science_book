import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.nonparametric.kde import KDEUnivariate

# import Zircon data from Puetz (2010)        
my_data = pd.read_excel('1-s2.0-S1674987117302141-mmc1.xlsx', sheet_name='Data')
my_data = my_data[(my_data.age206Pb_238U>0)&(my_data.age206Pb_238U<1500)]
my_sample = my_data.age206Pb_238U

# Plot the Density Histogram
fig, ax = plt.subplots(figsize=(8,5))
bins = np.arange(0,1500,20)
ax.hist(my_sample, bins, color='#c7ddf4', edgecolor='k', density=True, label='Density Histogram - bins = 20 My')

# Compute and plot the KDE
age_eval = np.arange(0,1500,10)
kde = KDEUnivariate(my_sample)
kde.fit(bw=20)
pdf = kde.evaluate(age_eval)
ax.plot(age_eval, pdf, label ='Gaussian KDE - bw = 20 Ma', linewidth=2, alpha=0.7, color='#ff464a')

# Adjust diagram parameters
ax.set_ylim(0,0.0018)
ax.set_xlabel('Age (My)')
ax.set_ylabel('Probability Densisty')
ax.legend()
ax.grid(axis='y')

# Plot mass extinction annotations
mass_extinction_age = [444, 359, 252, 66, 0]
pdf_mass_extinction_age = kde.evaluate(mass_extinction_age)
mass_extincyion_name = ["Ordovician-Silurian", "Late Devonian", "Permian-Triassic", "Cretaceous-Paleogene", "Triggered by Men?"]
y_offsets = [0.0001, 0.0001, 0.0002, 0.0002, 0.0004]
y_texts = [30, 105, 15, 62, 160]
x_texts = [30, 30, 30, 30, 30]

for x, y, name, x_text, y_text, y_offset in zip(mass_extinction_age, pdf_mass_extinction_age, mass_extincyion_name, x_texts, y_texts, y_offsets):
    ax.annotate(name, xy=(x, y + y_offset), xycoords='data',
    xytext=(x_text, y_text), textcoords='offset points',
    arrowprops=dict(arrowstyle="->",
    connectionstyle="angle, angleA=0, angleB=90, rad=10"))

fig.tight_layout()