import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,6)
y = np.array([0,1,2,9,9])

fig, ax = plt.subplots()
ax.scatter(x, y, marker = 'o', s = 100, color = '#c7ddf4', edgecolor = 'k')

orders = np.array([2,3,4])
colors =['#ff464a','#342a77','#4881e9']
linestiles = ['-','--','-.']

for order, color, linestile in zip(orders, colors, linestiles):   
    betas = np.polyfit(x, y, order)
    func = np.poly1d(betas)
    x1 = np.linspace(0.5,5.5, 1000)
    y1 = func(x1)
    ax.plot(x1, y1, color=color, linestyle=linestile, label="Linear model of order " + str(order))

ax.legend()    
ax.set_xlabel('A quantity relevant in geology\n(e.g., time)')
ax.set_ylabel('A quantity relevant in geology\n(e.g., spring flow rate)') 
fig.tight_layout()  
