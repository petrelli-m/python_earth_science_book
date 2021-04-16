epochs = ['one','two','three','three-b']

fig, ax = plt.subplots() 
for epoch in epochs:
    my_data = my_dataset1[(my_dataset1.Epoch == epoch)]
    ax.scatter(my_data.Zr, my_data.Th, label="Epoch " + epoch)

ax.set_title("My Third Diagram again")
ax.set_xlabel("Zr [ppm]")
ax.set_ylabel("Th [ppm]")
ax.legend()

