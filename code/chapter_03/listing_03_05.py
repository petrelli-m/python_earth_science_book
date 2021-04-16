fig, ax = plt.subplots() 

my_data1 = my_dataset1[(my_dataset1.Epoch == 'one')]
ax.scatter(my_data1.Zr, my_data1.Th, label='Epoch 1')

my_data2 = my_dataset1[(my_dataset1.Epoch == 'two')]
ax.scatter(my_data2.Zr, my_data2.Th, label='Epoch 2')

my_data3 = my_dataset1[(my_dataset1.Epoch == 'three')]
ax.scatter(my_data3.Zr, my_data3.Th, label='Epoch 3')

my_data4 = my_dataset1[(my_dataset1.Epoch == 'three-b')]
ax.scatter(my_data4.Zr, my_data4.Th, label='Epoch 3b')
    
ax.set_title("My Third Diagram")   
ax.set_xlabel("Zr [ppm]")
ax.set_ylabel("Th [ppm]")
ax.legend()

