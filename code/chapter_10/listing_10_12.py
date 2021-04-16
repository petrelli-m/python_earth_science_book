import pandas as pd
import matplotlib.pyplot as plt
import sympy as sym

a, b, sigma_a, sigma_b = sym.symbols("a b sigma_a sigma_b")

def symbolic_error_prop(func, val_a, val_sigma_a,  val_b=0,  val_sigma_b=0):
    
    z = sym.lambdify([a, b], func, 'numpy')
    sigma_z = sym.lambdify([a, b, sigma_a, sigma_b], sym.sqrt((sym.diff(func, a)**2 * sigma_a**2)+(sym.diff(func,b)**2 * sigma_b**2)), 'numpy')
    val_z = z(a=val_a, b=val_b)
    val_sigma_z = sigma_z(a=val_a, b=val_b, sigma_a=val_sigma_a, sigma_b=val_sigma_b)
    
    return val_z, val_sigma_z

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

ratio_y, sigma_ratio_y = symbolic_error_prop(a/b, val_a=my_dataset.Rb, val_sigma_a=my_dataset.Rb*0.1, val_b=my_dataset.Th,  val_sigma_b=my_dataset.Th*0.1)

my_dataset['Rb_Th'] = ratio_y
my_dataset['Rb_Th_1s'] = sigma_ratio_y 

epochs = ['one','two','three','three-b']
colors = ['#afbbb5', '#f10e4a', '#27449c', '#f9a20e']

fig, ax = plt.subplots()
for epoch, color in zip(epochs, colors):
    my_data = my_dataset[(my_dataset.Epoch == epoch)]
    ax.errorbar(x=my_data.La, y=my_data.Rb_Th, xerr=my_data.La*0.1, yerr=my_data.Rb_Th_1s, linestyle='', markerfacecolor= color, markersize=6, marker='o', markeredgecolor='k', ecolor=color, elinewidth=0.5, capsize=0, label="Epoch " + epoch)

ax.legend(title='CFC Recent Activity')
ax.set_ylabel('Rb/Th')
ax.set_xlabel('La [ppm]')
