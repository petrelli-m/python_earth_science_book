fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
plt.scatter(my_dataset.Zr, my_dataset.Th, marker='o', s=10, label="size 10")
ax1.set_xlabel("Zr [ppm]")
ax1.set_ylabel("Th [ppm]")
ax1.set_xlim([100, 1000])
ax1.set_ylim([0, 100])
ax1.legend()

ax2 = fig.add_subplot(2, 2, 2)
ax2.scatter(my_dataset.Zr, my_dataset.Th, marker='o', s=50, label="size 50")
ax2.set_xlabel("Zr [ppm]")
ax2.set_ylabel("Th [ppm]")
ax2.set_xlim([100, 1000])
ax2.set_ylim([0, 100])
ax2.legend()

ax3 = fig.add_subplot(2, 2, 3)
ax3.scatter(my_dataset.Zr, my_dataset.Th, marker='o', s=100, label="size 100")
ax3.set_xlabel("Zr [ppm]")
ax3.set_ylabel("Th [ppm]")
ax3.set_xlim([100, 1000])
ax3.set_ylim([0, 100])
ax3.legend()

ax4 = fig.add_subplot(2, 2, 4)
ax4.scatter(my_dataset.Zr, my_dataset.Th, marker='o', s=200, label="size 200")
ax4.set_xlabel("Zr [ppm]")
ax4.set_ylabel("Th [ppm]")
ax4.set_xlim([100, 1000])
ax4.set_ylim([0, 100])
ax4.legend()

fig.tight_layout()
