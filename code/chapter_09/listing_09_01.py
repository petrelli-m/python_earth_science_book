from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np 


# I'm going to define my normal PDF...
def normal_pdf(x, mean, std):
    return 1/(np.sqrt(2*np.pi*std**2))*np.exp(-0.5*((x - mean)**2)/(std**2))


x = np.arange(-12, 12, .001)

pdf1 = normal_pdf(x, mean=0, std=2)

#the built-in norm PDF in scipy.stats
pdf2 = norm.pdf(x, loc=0, scale=2)

fig = plt.figure(figsize=(7,9))
ax1 = fig.add_subplot(3, 1, 1)
ax1.plot(x,pdf1, color='#84b4e8', linestyle="-", linewidth=6, label="My normal PDF")
ax1.plot(x,pdf2, color='#ff464a', linestyle="--", label="norm.pdf() in scipy.stats ")
ax1.set_xlabel("x")
ax1.set_ylabel("PDF(x)")
ax1.legend(title = r"Normal PDF with $\mu$=0 and 1$\sigma$=2")


ax2 = fig.add_subplot(3, 1, 2)
for i in [1, 2, 3]:
     y = normal_pdf(x,0,i)
     ax2.plot(x, y, label=r"$\mu$ = 0, 1$\sigma$ = " + str(i))
ax2.set_xlabel("x")
ax2.set_ylabel("PDF(x)")
ax2.legend()

ax3 = fig.add_subplot(3, 1, 3)
for i in [-3, 0, 3]:
     y = normal_pdf(x, i, 1)
     ax3.plot(x, y, label=r"$\mu$ = " + str(i) + ", 1$\sigma$ = 1")
ax3.set_xlabel("x")
ax3.set_ylabel("PDF(x)")
ax3.legend()

fig.tight_layout()