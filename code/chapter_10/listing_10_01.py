import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

my_dataset = pd.read_excel('USGS_BCR2G.xls', sheet_name='Sheet1')

fig, ax = plt.subplots()
ax.hist(my_dataset.La, bins='auto', density=True, edgecolor='#000000', color='#c7ddf4', label="USGS BCR2G")
ax.set_xlabel("La [ppm]")
ax.set_ylabel("Probability Density")

x = np.linspace(23,27.5,500)
pdf = stats.norm(loc=my_dataset.La.mean(), scale=my_dataset.La.std()).pdf(x)

ax.plot(x,pdf, linewidth=2, color='#ff464a', label='Normal Distribution')

ax.legend()
