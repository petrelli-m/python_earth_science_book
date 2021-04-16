fig, ax = plt.subplots()
ax.hist(my_dataset.Zr, bins='auto', density=True, histtype='step', linewidth=2, cumulative=1, color='tab:blue')
ax.set_xlabel('Zr [ppm]')
ax.set_ylabel('Likelihood of occurrence')
