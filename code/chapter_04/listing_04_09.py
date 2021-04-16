import pandas as pd
import matplotlib.pyplot as plt

myDataset1 = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

x = myDataset1.Zr
y = myDataset1.Th


loc_parameters = ['upper right'	, 'upper left', 'lower left', 'lower right','center'	,'center left']

fig = plt.figure(figsize=(8,4))
for i in range(len(loc_parameters)):
    ax = fig.add_subplot(2,3,i+1)
    ax.scatter(x, y, marker = 's', color = '#c7ddf4', edgecolor = '#000000', label="loc = " + loc_parameters[i])
    ax.set_xlabel("Zr [ppm]")
    ax.set_ylabel("Th [ppm]")
    ax.legend(loc=loc_parameters[i])

fig.tight_layout()
