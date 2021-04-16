import pandas as pd
import seaborn as sns

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

my_dataset1 = my_dataset[['Ba', 'Zr', 'Th']]
sns.pairplot(my_dataset1)
