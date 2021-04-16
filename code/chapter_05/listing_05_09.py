import pandas as pd

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

statistics = my_dataset[['Ba','Sr','Zr','La']].describe()

print(statistics)

'''
Output:
                Ba           Sr          Zr          La
count   370.000000   369.000000  370.000000  370.000000
mean    789.733259   516.422115  365.377397   74.861088
std     523.974960   241.922439  118.409962   18.256772
min       0.000000     9.541958  185.416567   45.323289
25%     297.402777   319.667551  274.660242   61.745228
50%     768.562055   490.111131  339.412064   71.642167
75%    1278.422645   728.726116  438.847368   83.670805
max    2028.221963  1056.132069  920.174406  169.550008
'''   