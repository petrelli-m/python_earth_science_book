import statsmodels.api as sm

fig = plt.figure()

ax1 = fig.add_subplot(1, 2, 1)
sm.qqplot(data=MnO, fit = True, line="45", ax=ax1, markerfacecolor='#4881e9', markeredgewidth='0.5', markeredgecolor='k', label='MnO')
ax1.set_aspect('equal', 'box')
ax1.legend(loc='lower right')

ax2 = fig.add_subplot(1, 2, 2)
sm.qqplot(data=Pb, fit = True, line="45", ax=ax2, markerfacecolor='#4881e9', markeredgewidth='0.5', markeredgecolor='k', label='Pb')
ax2.set_aspect('equal', 'box')
ax2.legend(loc='lower right')

fig.tight_layout()