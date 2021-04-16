import numpy as np
import matplotlib.pyplot as plt


def normal_pdf(x, mu, sigma):
    pdf = 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2 / (2*sigma**2))
    return pdf

signa_levels = [1, 2, 3]
confidences = [68.27, 95.45, 99.73]

fig = plt.figure(figsize=(7,8))

my_mean = my_dataset.La.mean()
my_std = my_dataset.La.std()

x_pdf = np.linspace(my_mean - 4 * my_std, my_mean + 4 * my_std, 1000)
my_pdf = normal_pdf(x_pdf, my_mean, my_std)

for signa_level, confidence in zip(signa_levels,confidences):
    ax = fig.add_subplot(3, 1, signa_level)
    ax.hist(my_dataset.La, bins='auto', density=True, edgecolor='#000000', color='#c7ddf4', label='USGS BCR2G', zorder=0)
    x_confidence = np.linspace(my_mean - signa_level * my_std, my_mean + signa_level * my_std, 1000)
    ax.plot(x_pdf, my_pdf, linewidth=2, color='#ff464a', label='Normal Distribution', zorder=1)
    ax.fill_between(x_confidence, normal_pdf(x_confidence, my_mean, my_std), y2=0, color='#ff464a', alpha=0.2, label='prob. = {}'.format(confidence) + ' %', zorder=1)
    ax.legend(ncol=3, loc='upper center', title=r'$\mu~ \pm ~$' + str(signa_level) + r'$ ~ \sigma ~ $ = ' + '{:.1f}'.format(my_mean) + r'$~ \pm ~$' + '{:.1f}'.format(signa_level * my_std))
    ax.set_ylim(0,1.6)
    ax.set_xlabel('La [ppm]')
    ax.set_ylabel('prob. dens.')

fig.tight_layout()