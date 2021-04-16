import pandas as pd
import matplotlib.pyplot as plt

my_dataset = pd.read_excel(
    'Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

fig, ax = plt.subplots()
ax.hist(my_dataset.Zr, bins='auto', edgecolor='black', color='tab:blue', alpha=0.8)
ax.set_xlabel('Zr [ppm]')
ax.set_ylabel('Counts')
