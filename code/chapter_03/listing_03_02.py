import pandas as pd
import matplotlib.pyplot as plt

my_dataset1 = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

x = my_dataset1.Zr
y = my_dataset1.Th

fig, ax = plt.subplots() # Create a figure containing one axes
ax.scatter(x, y)

