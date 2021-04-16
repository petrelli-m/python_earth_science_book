import matplotlib.pyplot as plt

fig = plt.figure()

for i in range(1, 7):
    ax = fig.add_subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha='center')

plt.tight_layout()
