my_mean = my_dataset.La.mean()
R = 25.6
accuracy = 100 * (my_mean - R) / R
my_std = my_dataset.La.std()
precision = 100 * my_std / R

fig, ax = plt.subplots(figsize=(6,5))
ax.hist(my_dataset.La, bins = 'auto', density = True, edgecolor = '#000000', color = '#c7ddf4', label = 'USGS BCR2G')
ax.set_xlabel('La [ppm]')
ax.set_ylabel('Probability Density')

ax.axvline(x=my_dataset.La.mean(), color='#ff464a', linewidth=3, label='Mean of the Measurements:' + str(round(my_mean, 1)) + '[ppm]')
ax.axvline(x = R, color='#342a77', linewidth=3, label='Accepded Value')

ax.axvline(x = my_mean - my_std, color = '#4881e9', linewidth = 1)
ax.axvline(x = my_mean + my_std, color = '#4881e9', linewidth = 1)
ax.axvspan(my_mean - my_std,  my_mean + my_std, alpha = 0.2, color = '#342a77', label = r'$1\sigma$')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=False, shadow=False, ncol=2, title = 'Accuracy = {:.1f} % - Precision = {:.1f} %'.format(accuracy, precision))

fig.tight_layout()
