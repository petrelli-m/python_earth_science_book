import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,6))

dists = [stats.uniform(loc=0.5, scale=2), stats.norm(loc=1.5, scale=0.5), stats.laplace(loc=1.5, scale=0.6)]
names = ['Uniform', 'Normal', 'Laplace']
x = np.linspace(0,3,1000)

for i, (dist, name) in enumerate(zip(dists, names)):
    
    # Probability Density Function (pdf)
    pdf = dist.pdf(x)
    ax1 = fig.add_subplot(3, 3, 3*i+1)
    ax1.plot(x, pdf, color='#4881e9', label= name + ' PDF')
    ax1.set_xlim(0,3)
    ax1.set_ylim(0,1.5)
    ax1.set_xlabel('Variable, x')
    ax1.set_ylabel('Prob. Dens.')
    ax1.legend()
    
    #Distribution (rnd) of the Random Variable based on the selected pdf
    rnd = dist.rvs(size=5000)
    ax2 = fig.add_subplot(3, 3, 3*i+2)
    ax2.hist(rnd, bins='auto', color='#84b4e8', edgecolor='#000000')
    ax2.set_xlim(0,3)
    ax2.set_ylim(0,400)
    ax2.set_xlabel('Variable, x')
    ax2.set_ylabel('Occurrences')
    
    ax3 = fig.add_subplot(3, 3, 3*i+3)
    mean_dist = []
    for _ in range(1000):
        mean_dist.append(dist.rvs(size=3).mean())
    mean_dist = np.array(mean_dist)
    ax3.hist(mean_dist, density=True, bins='auto',  color='#84b4e8', edgecolor='#000000')
    normal = stats.norm(loc= mean_dist.mean(), scale= mean_dist.std())
    ax3.plot(x, normal.pdf(x), color='#ff464a')
    ax3.set_xlim(0,3)
    ax3.set_ylim(0,1.5)
    ax3.set_xlabel('Mean')
    ax3.set_ylabel('Prob. Dens.')
    
fig.tight_layout()