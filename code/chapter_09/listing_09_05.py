from statsmodels.nonparametric.kde import KDEUnivariate
import matplotlib.pyplot as plt
import numpy as np

kernels = ['gau', 'epa', 'uni', 'tri', 'biw', 'triw']
kernels_names = ['Gaussian', 'Epanechnikov', 'Uniform', 'Triangular', 'Biweight', 'Triweight']
positions = np.arange(1,9,1)

fig, ax = plt.subplots()

for kernel, kernel_name, pos in zip(kernels, kernels_names, positions):

    # kernels
    kde = KDEUnivariate([0])
    kde.fit(kernel= kernel, bw=1,  fft=False, gridsize=2**10)
    ax.plot(kde.support, kde.density, label = kernel_name, linewidth=1.5, alpha=0.8)

ax.set_xlim(-2,2)
ax.grid()
ax.legend(title='kernel functions')

