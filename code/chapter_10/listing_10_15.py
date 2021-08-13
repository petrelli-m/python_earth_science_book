import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mean, std):
    return 1/(np.sqrt(2*np.pi*std**2))*np.exp(-0.5*(((x - mean)**2)/(std**2)))

my_a, my_sigma_a = 40, 8 
my_b, my_sigma_b = 20, 2 

n = 10000
a_normal = np.random.default_rng().normal(my_a, my_sigma_a, n)
b_normal = np.random.default_rng().normal(my_b, my_sigma_b, n)   

# Linearized Method
my_sum_ab_l, my_sigma_sum_ab_l = sum_ab(a=my_a, b=my_b, sigma_a=my_sigma_a, sigma_b=my_sigma_b)
my_x = np.linspace(20, 100, 1000)
my_sum_ab_PDF = gaussian(x=my_x, mean=my_sum_ab_l, std=my_sigma_sum_ab_l)

# Monte Carlo estimation
my_sum_ab_mc =  a_normal + b_normal
my_sum_ab_mc_mean = my_sum_ab_mc.mean()
my_sigma_sum_ab_mc_std = my_sum_ab_mc.std()
 
fig, ax = plt.subplots()
ax.hist(my_sum_ab_mc, bins='auto', color='#c7ddf4', edgecolor='k', density=True, label= r'a+b sample distribution by MC ($\mu_{a+b} = $' + "{:.0f}".format(my_sum_ab_mc_mean) + r'  - 1$\sigma_{a+b} = $' + "{:.0f}".format(my_sigma_sum_ab_mc_std) + ')')
ax.plot(my_x, my_sum_ab_PDF, color='#ff464a', linestyle='--', label=r'a+b PDF by linearized error propagation ($\mu_{a+b} = $' + "{:.0f}".format(my_sum_ab_l) + r'  - 1$\sigma_{a+b} = $' + "{:.0f}".format(my_sigma_sum_ab_l) + ')')
ax.set_xlabel('a + b')
ax.set_ylabel('Probability Density')
ax.legend(title='Error Propagation')
ax.set_ylim(0,0.07)

fig.tight_layout()


