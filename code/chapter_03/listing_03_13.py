import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm

my_data = pd.read_csv('DEM.csv')
fig, ax = plt.subplots() 
ax.scatter(x = my_data.X_LOC.values, 
           y = my_data.Y_LOC.values, 
           c=my_data.ELEVATION.values, 
           s=2, cmap='hot', linewidth=0, marker='o')
ax.axis('equal')
ax.axis('off')
colorbar = fig.colorbar(cm.ScalarMappable(cmap='hot'), extend='max', ax=ax)
colorbar.set_label('Elevation [m]', rotation=270, labelpad=20)
colorbar.outline.set_edgecolor('Grey')