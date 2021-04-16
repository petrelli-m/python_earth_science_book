import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

mu = 0 # mean 
sigma = 1 # standard deviation
normal_sample = np.random.normal(mu, sigma, 15000)

# plot the histogram of the sample distribution
fig, ax = plt.subplots()
ax.hist(normal_sample, bins='auto', density=True, color='#c7ddf4', edgecolor='#000000', label='Random sample with normal distribution')

# probability density function
x = np.arange(-5,5, 0.01)
normal_pdf = norm.pdf(x, loc= mu, scale = sigma)
ax.plot(x, normal_pdf, color='#ff464a', linewidth=1.5, linestyle='--', label=r'Normal PDF with $\mu$=0 and 1$\sigma$=1')
ax.legend(title='Normal Distribution')
ax.set_xlabel('x')
ax.set_ylabel('Probability Density')
ax.set_xlim(-5,5)
ax.set_ylim(0,0.6)

# Descriptive statistics
aritmetic_mean = normal_sample.mean()
standard_deviation = normal_sample.std()

print('Sample mean equal to {:.4f}'.format(aritmetic_mean))
print('Sample standard deviation equal to {:.4f}'.format(standard_deviation))

'''
Output: (your results will be sighly different because of the pseudo-random nature of the distribution)
Sample mean equal to -0.0014
Sample standard deviation equal to 1.0014
'''


