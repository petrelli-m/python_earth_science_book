scaler = StandardScaler().fit(X0_train)
X_train = scaler.transform(X0_train)

fig2 = plt.figure(figsize=(8,8))
for i in range(0,12):
    ax3 = fig2.add_subplot(4, 3, i+1)
    sns.kdeplot(X_train[:, i],fill=True, color='k', facecolor='#ffdfab', ax = ax3)
    ax3.set_xlabel('scaled ' + x_labels_melt[i] + ' the melt')
fig2.align_ylabels()
fig2.tight_layout()

fig3 = plt.figure(figsize=(6,8))
for i in range(0,10):
    ax4 = fig3.add_subplot(5, 2, i+1)
    sns.kdeplot(X_train[:, i+12],fill=True, color='k', facecolor='#ffdfab', ax = ax4)
    ax4.set_xlabel('scaled ' + x_labels_cpx[i] + ' in cpx')
fig3.align_ylabels()
fig3.tight_layout()
