import numpy as np
import matplotlib.pyplot as plt

def normal_pdf(x, mu, sigma):
    pdf = 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2 / (2*sigma**2))
    return pdf

def unifrom_pdf(x, a, b):
    pdf = np.piecewise(x, [(x>=a) & (x<=b), (x<a) & (x>b)], [1/(b-a), 0])
    return pdf

# Random sampling of a normal distribution
my_mu, my_sigma = 0, 0.1 # mean and standard deviation
sn = np.random.default_rng().normal(loc=my_mu, scale=my_sigma, size=10000)
fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax1.hist(sn, density=True, bins='auto', edgecolor='k', color='#c7ddf4', label='Random Sampling of the Normal Distribution')
my_xn = np.linspace(my_mu - 4 * my_sigma, my_mu + 4 * my_sigma, 1000)
my_yn = normal_pdf(x=my_xn, mu=my_mu, sigma=my_sigma)
ax1.plot(my_xn, my_yn,linewidth=2, linestyle='--', color='#ff464a', label='Target Normal Probability Density Function')
ax1.set_ylim(0.0, 7.0)
ax1.set_xlabel('x')
ax1.set_ylabel('Prob. Density')
ax1.legend()

# Random sampling of a uniform distribution
my_a, my_b = -1, 1 # lower and upper bound of the uniform distribution
su = np.random.default_rng().uniform(low=my_a, high=my_b, size=10000)
ax2 = fig.add_subplot(2, 1, 2)
ax2.hist(su, density=True, bins='auto', edgecolor='k', color='#c7ddf4', label='Random Sampling of the Uniform Distribution')
my_xu = np.linspace(-2, 2, 1000)
my_yu = unifrom_pdf(x=my_xu, a=my_a, b=my_b)
ax2.plot(my_xu, my_yu, linewidth=2, linestyle='--', color='#ff464a', label='Target Uniform Probability Density Function')
ax2.set_ylim(0, 1)
ax2.set_xlabel('x')
ax2.set_ylabel('Prob. Density')
ax2.legend()

fig.tight_layout()
