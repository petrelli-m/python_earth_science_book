import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

my_sub_dataset = my_dataset[['Ce','La','U','Sc']]

cov = my_sub_dataset.cov()
cor = my_sub_dataset.corr()

fig = plt.figure(figsize=(11,5))

ax1 = fig.add_subplot(1,2,1)
ax1.set_title('Covariance Matrix')
sns.heatmap(cov, annot=True, cmap='cividis', ax=ax1)

ax2 = fig.add_subplot(1,2,2)
ax2.set_title('Correlation Matrix')
sns.heatmap(cor, annot=True, vmin= -1, vmax=1,  cmap='coolwarm', ax=ax2)

fig.tight_layout()

