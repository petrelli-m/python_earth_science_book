import pandas as pd
import matplotlib.pyplot as plt

my_dataset = pd.read_excel(
    'Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

epochs = ['one', 'two', 'three', 'three-b']
colors = ['#c8b4ba', '#f3ddb3', '#c1cd97', '#e18d96']
markers = ['o', 's', 'd', 'v']

fig, ax = plt.subplots()
for (epoch, color, marker) in zip(epochs, colors, markers):
    my_data = my_dataset[(my_dataset.Epoch == epoch)]
    ax.scatter(my_data.Zr, my_data.Th, marker=marker, s=50, c=color, edgecolor='0', label="Epoch " + epoch)

ax.set_xlabel("Zr [ppm]")
ax.set_ylabel("Th [ppm]")
ax.legend(title="Phlegraean Fields \n Age < 15 ky")
