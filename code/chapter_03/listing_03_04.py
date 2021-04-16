# Define two sub-dataset for Zr>450 and Zr<450 respectively 
my_sub_dataset1 = my_dataset1[my_dataset1.Zr > 450] 
my_sub_dataset2 = my_dataset1[my_dataset1.Zr < 450]

#generate a new picture 
fig, ax = plt.subplots() 
# Generate the scatter Zr Vs Th diagram for Zr > 450 
# in blue also defining the legend caption as "Zr > 450 [ppm]"  
x1 = my_sub_dataset1.Zr
y1 = my_sub_dataset1.Th
ax.scatter(x1, y1, color='blue', label="Zr > 450 [ppm]") 
# Generate the scatter Zr Vs Th diagram for Zr < 450 
# in red also defining the legend caption as "Zr < 450 [ppm]"
x2 = my_sub_dataset2.Zr
y2 = my_sub_dataset2.Th
ax.scatter(x2, y2, color='red', label="Zr < 450 [ppm]")

ax.set_title("My Second Diagram")
ax.set_xlabel("Zr [ppm]")
ax.set_ylabel("Th [ppm]")
# generate the legend
ax.legend()

