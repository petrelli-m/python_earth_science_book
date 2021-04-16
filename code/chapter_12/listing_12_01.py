import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import mean_squared_error 
from sklearn.metrics import r2_score

# Import The Training Data Set
my_training_dataset = pd.read_excel('GlobalDataset_Final_rev9_TrainValidation.xlsx', usecols = "A:M,O:X,Z:AA", skiprows=1, engine='openpyxl')
my_training_dataset.columns = [c.replace('.1', 'cpx') for c in my_training_dataset.columns]
my_training_dataset = my_training_dataset.fillna(0)

train_labels = np.array([my_training_dataset.Sample_ID]).T
X0_train = my_training_dataset.iloc[:, 1:23]
Y_train = np.array([my_training_dataset.T_K]).T

fig = plt.figure(figsize=(8,8))
x_labels_melt = [r'SiO$_2$', r'TiO$_2$', r'Al$_2$O$_3$', r'FeO$_t$', r'MnO', r'MgO', r'CaO', r'Na$_2O$', r'K$_2$O', r'Cr$_2$O$_3$', r'P$_2$O$_5$', r'H$_2$O']
for i in range(0,12):
    ax1 = fig.add_subplot(4, 3, i+1)
    sns.kdeplot(X0_train.iloc[:, i],fill=True, color='k', facecolor='#c7ddf4', ax = ax1)
    ax1.set_xlabel(x_labels_melt[i] + ' [wt. %] the melt')
fig.align_ylabels()
fig.tight_layout()

fig1 = plt.figure(figsize=(6,8))
x_labels_cpx = [r'SiO$_2$', r'TiO$_2$', r'Al$_2$O$_3$', r'FeO$_t$', r'MnO', r'MgO', r'CaO', r'Na$_2O$', r'K$_2$O', r'Cr$_2$O$_3$']
for i in range(0,10):
    ax2 = fig1.add_subplot(5, 2, i+1)
    sns.kdeplot(X0_train.iloc[:, i+12],fill=True, color='k', facecolor='#c7ddf4', ax = ax2)
    ax2.set_xlabel(x_labels_cpx[i] + ' [wt. %] in cpx')
fig1.align_ylabels()
fig1.tight_layout()







