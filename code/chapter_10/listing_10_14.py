import numpy as np
import matplotlib.pyplot as plt

def normal_pdf(x, mu, sigma):
    pdf = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x - mu)**2 / (2 * sigma**2))
    return pdf

fig = plt.figure(figsize=(6,9))

# Random sampling of a normal distribution
my_mu, my_sigma = 0, 0.1 # mean and standard deviation

bit_generators = [np.random.MT19937(), np.random.Philox(), np.random.SFC64()]
names = ['Mersenne Twister PRNG (MT19937)', 'Philox (4x64) PRNG (Philox)', 'Chris Doty-Humphrey\'s SFC PRNG (SFC64)']
indexes = [1,2,3]

for bit_generator, name, index in zip(bit_generators, names, indexes):
    sn = np.random.Generator(bit_generator).normal(loc = my_mu, scale = my_sigma, size = 10000)
    ax = fig.add_subplot(3, 1, index)
    ax.hist(sn, density=True, bins='auto', edgecolor='k', color='#c7ddf4', label=name)
    my_xn = np.linspace(my_mu - 4 * my_sigma, my_mu + 4 * my_sigma, 1000)
    my_yn = normal_pdf(x=my_xn, mu=my_mu, sigma=my_sigma)
    ax.plot(my_xn, my_yn, linewidth=2, linestyle='--', color='#ff464a', label ='Target Normal PDF')
    ax.set_ylim(0.0, 7.0)
    ax.set_xlim(my_mu - 6 * my_sigma, my_mu + 6 * my_sigma)
    ax.set_xlabel('x')
    ax.set_ylabel('Probability Density')
    ax.legend()

fig.tight_layout()

