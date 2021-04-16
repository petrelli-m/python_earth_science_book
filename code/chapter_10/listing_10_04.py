import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

mean_value = 1.5
std_dev = 0.5
dist = stats.norm(loc=mean_value, scale=std_dev) 
x = np.linspace(0, 3, 1000)
fig = plt.figure(figsize=(6,8))

# Distribution of the Random Variable based on the normal PDF
pdf = dist.pdf(x)
ax1 = fig.add_subplot(3, 1, 1)
ax1.plot(x, pdf, color='#84b4e8', label =r'$\mu_p$ = 1.5 - 1$\sigma_p$ = 0.5')
ax1.set_xlim(0,3)
ax1.set_ylim(0,1)
ax1.set_xlabel('Variable, x')
ax1.set_ylabel('Prob. Dens.')
ax1.legend(title = 'Parent Distribution')

# Dependence of the SE on the Central Limit Theorem
ax2 = fig.add_subplot(3, 1, 2)
std_of_the_mean = []
ns = [2, 10, 100, 500]

for n in ns:
    # Mean Estimation Based on 1000 attempts using N values
    mean_dist = []
    for _ in range(1000):
        mean_dist.append(dist.rvs(size=n).mean())
    mean_dist = np.array(mean_dist)
    std_of_the_mean.append(mean_dist.std())
    normal = stats.norm(loc=mean_dist.mean(), scale=mean_dist.std())
    ax2.plot(x, normal.pdf(x), label='N = ' + str(n))     
ax2.set_xlim(0, 3)
ax2.set_xlabel('Mean')
ax2.set_ylabel('Prob. Dens.')
ax2.legend(title='Standard Deviation of the Means', ncol=2)   

# SE estimates and the empirically derived std of the Means
ax3 = fig.add_subplot(3, 1, 3)
ax3.scatter(ns, std_of_the_mean, color='#ff464a', edgecolor='#000000', label='Standard Deviation of the Means', zorder = 1)
n1 = np.linspace(1, 600, 600)
se = std_dev / np.sqrt(n1)
ax3.plot(n1 , se, c='#4881e9', label='Standard Error (SE)', zorder=0)
ax3.set_xlabel('N')
ax3.set_ylabel('Standard Error, SE')
ax3.legend()
fig.tight_layout()



