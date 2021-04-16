import matplotlib.pyplot as plt

fig = plt.figure()
# index 1
ax1 = fig.add_subplot(2, 3, 1)
ax1.text(0.5, 0.5, str((2, 3, 1)), fontsize=18, ha='center')

# index 2
ax1 = fig.add_subplot(2, 3, 2)
ax1.text(0.5, 0.5, str((2, 3, 2)), fontsize=18, ha='center')

# index 3
ax1 = fig.add_subplot(2, 3, 3)
ax1.text(0.5, 0.5, str((2, 3, 3)), fontsize=18, ha='center')

# index 4
ax1 = fig.add_subplot(2, 3, 4)
ax1.text(0.5, 0.5, str((2, 3, 4)), fontsize=18, ha='center')

# index 5
ax1 = fig.add_subplot(2, 3, 5)
ax1.text(0.5, 0.5, str((2, 3, 5)), fontsize=18, ha='center')

# index6
ax1 = fig.add_subplot(2, 3, 6)
ax1.text(0.5, 0.5, str((2, 3, 6)), fontsize=18, ha='center')

plt.tight_layout()