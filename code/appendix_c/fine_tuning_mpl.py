import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, AutoMinorLocator
import pandas as pd
import numpy as np

myDataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

fig, ax = plt.subplots()
# Figure managment
# https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html

# Axes managment
# https://matplotlib.org/stable/api/axes_api.html

# select your style
#  https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
mpl.style.use('ggplot')

# Make the plot
ax.hist(myDataset.Zr, density=True, bins='auto', color='Tab:blue', edgecolor='k', alpha=0.8, label = 'CFC recent activity')

# Commonnly used personalizations
ax.set_xlabel('Zr [ppm]')
ax.set_ylabel('Probability density')
ax.set_title('Zr sample distribution')
ax.set_xlim(-100, 1100)
ax.set_ylim(0,0.0055)
ax.set_xlabel(r'Zr [$\mu \cdot g^{-1}$]')
ax.set_ylabel('Probability density')
ax.set_xticks(np.arange(0, 1100 + 1, 250))  # adjust the x tick frequency
ax.set_yticks(np.arange(0, 0.0051, .001))  # adjust the y tick frequency


# Major and minor ticks
# https://matplotlib.org/stable/gallery/ticks_and_spines/major_minor_demo.html

ax.xaxis.set_minor_locator(AutoMinorLocator())

ax.tick_params(which='both', width=1)
ax.tick_params(which='major', length=7)
ax.tick_params(which='minor', length=4)

ax.yaxis.set_minor_locator(MultipleLocator(0.0005))

ax.tick_params(which='both', width=1)
ax.tick_params(which='major', length=7)
ax.tick_params(which='minor', length=4)


# Spine management
# https://matplotlib.org/stable/api/spines_api.html

ax.spines["top"].set_color("#363636")
ax.spines["right"].set_color("#363636")
ax.spines["left"].set_color("#363636")
ax.spines["bottom"].set_color("#363636")

# Spine placement
# https://matplotlib.org/stable/gallery/ticks_and_spines/spine_placement_demo.html

# Advanced Annotations
# https://matplotlib.org/stable/tutorials/text/annotations.html#plotting-guide-annotation
ax.annotate("Mean Value",
            xy=(myDataset.Zr.mean(), 0.0026), xycoords='data',
            xytext=(myDataset.Zr.mean() + 250, 0.0035), textcoords='data',
            arrowprops=dict(arrowstyle="fancy",
                            color="0.5",
                            shrinkB=5,
                            connectionstyle="arc3,rad=0.3",
                            ),
            )

ax.annotate("Modal \n value ",
            xy=(294, 0.0045), xycoords='data',
            xytext=(0, 0.005), textcoords='data',
            arrowprops=dict(arrowstyle="fancy",
                            color="0.5",
                            shrinkB=5,
                            connectionstyle="arc3,rad=-0.3",
                            ),
            )

# Legend
# https://matplotlib.org/stable/api/legend_api.html
ax.legend(title = 'My Legend')

fig.tight_layout()