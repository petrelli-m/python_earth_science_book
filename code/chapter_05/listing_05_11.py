import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

fig, ax = plt.subplots()
ax = sns.boxplot(x="Epoch", y="Zr", data=my_dataset,  palette="Set3")
