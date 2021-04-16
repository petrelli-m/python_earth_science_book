import matplotlib.pyplot as plt
import numpy as np 
from scipy.stats import norm, lognorm

colors = ['#342a77', '#ff464a', '#4881e9']
normal_mu = [0,0.5,1]
normal_sigma = [0.5,0.4,0.3]
x = np.arange(0.001, 7, .001) # for the log-normal PDF
x1 = np.arange(-2.5, 2.5, .001)  # for the normal PDF

fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, figsize = (8,9))

for mu_n, sigma_n, color in zip(normal_mu, normal_sigma, colors):   
     lognorm_pdf = lognorm.pdf(x, s=sigma_n, scale=np.exp(mu_n))
     r = lognorm.rvs(s=sigma_n, scale=np.exp(mu_n), size=15000)
     ax1.plot(x, lognorm_pdf, color=color, label=r"$\mu_n$ = " + str(mu_n) + r" - $\sigma_n$ = " + str(sigma_n))
     ax1.hist(r, bins='auto', density=True, color=color, edgecolor='#000000', alpha=0.5)
     logr= np.log(r)
     normal_pdf = norm.pdf(x1, loc= mu_n, scale = sigma_n)
     ax2.plot(x1, normal_pdf, color=color, label=r"$\mu_n$ = " + str(mu_n) + r" - $\sigma_n$ = " + str(sigma_n))
     ax2.hist(logr, bins='auto', density=True, color=color, edgecolor='#000000', alpha=0.5)
     my_mu = logr.mean()
     ax2.axvline(x=my_mu, color=color, linestyle="--", label=r"calculated $\mu_n$ = " + str(round(my_mu,3)))
     my_sigma = logr.std()
     print("Expected mean: " + str(mu_n) + " - Calculated mean: " + str(round(my_mu,3)))
     print("Expected std.dev.: " + str(sigma_n) + " - Calculated std.dev.: " + str(round(my_sigma,3)))
     
ax1.legend(title="log-normal distributions")   
ax1.set_xlabel('x')  
ax1.set_ylabel('Probability Density')  
ax2.legend(title="normal distributions") 
ax2.set_xlabel('ln(x)') 
ax2.set_ylabel('Probability Density')  

fig.tight_layout()





