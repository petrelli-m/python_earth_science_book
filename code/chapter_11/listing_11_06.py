import pandas as pd
import numpy as np
import statsmodels.api as st
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name=1)
el = 'Pb'

my_sub_dataset = my_dataset[my_dataset.Epoch == 'three-b']
my_sub_dataset = my_sub_dataset.dropna(subset=[el])

norms = [st.robust.norms.HuberT(t=1.345), st.robust.norms.Hampel(a=2.0, b=4.0, c=8.0)]
loc_labels = %*[r"Huber’s T function", r"Hampel function"]*)
indexes = [1,2]

fig = plt.figure(figsize=(6,6))

for norm, loc_label, index in zip(norms, loc_labels, indexes):

    huber_proposal_2 = st.robust.Huber(c= 1.5, norm = norm)
    h_loc, h_scale = huber_proposal_2(my_sub_dataset[el])
    ax = fig.add_subplot(2, 1, index)
    bins = np.arange(50,250,5)
    ax.hist(my_sub_dataset[el], density = True, edgecolor='k',  color='#4881e9', bins=bins)
    ax.axvline(h_loc, color = '#ff464a', linewidth = 2, label= loc_label + " as $\psi$: location at {:.1f} [ppm]".format(h_loc))
    ax.axvline(h_loc + h_scale, color = '#ebb60d')
    ax.axvline(h_loc - h_scale, color = '#ebb60d')
    ax.axvspan(h_loc + h_scale, h_loc - h_scale, alpha=0.1, color='orange', label="Huber's estimation for the scale: {:.1f} [ppm]".format(h_scale))
    ax.set_xlabel(el + " [ppm]")
    ax.set_ylabel('probability density')
    ax.set_ylim(0, 0.1)
    ax.legend(loc = 'upper right')
    ax.annotate('Large oulier at about 800 ppm', (253, 0.04), (230,0.04), ha='right', va='center', size=9, arrowprops=dict(arrowstyle='fancy'))
fig.tight_layout()
 
    