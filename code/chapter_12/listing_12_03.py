# Define the regressor, in our case the Extra Tree Regressor
regr = ExtraTreesRegressor(n_estimators=550, criterion='mse', max_features=22, random_state=280) # random_state fixed for reproducibility

# Train the model
regr.fit(X_train, Y_train.ravel())

# Import the test data set 
my_test_dataset = pd.read_excel('GlobalDataset_Final_rev9_Test.xlsx', usecols = "A:M,O:X,Z:AA", skiprows=1, engine='openpyxl')
my_test_dataset.columns = [c.replace('.1', 'cpx') for c in my_test_dataset.columns]
my_test_dataset = my_test_dataset.fillna(0)

X0_test = my_test_dataset.iloc[:, 1:23]
Y_test= np.array([my_test_dataset.T_K]).T
labels_test = np.array([my_test_dataset.Sample_ID]).T

# Scale the test dataset
X_test_scaled = scaler.transform(X0_test)

# Make the prediction on the test data set
predicted = regr.predict(X_test_scaled)   

# Evaluate the results using the R2 and RMSE 
r2 = r2_score(Y_test, predicted)
rmse = np.sqrt(mean_squared_error(predicted, Y_test))

# Plot data       
fig, ax = plt.subplots(figsize=(6,6))
ax.plot([1050,1850],[1050,1850], c='#000000', linestyle='--')
ax.scatter(Y_test,predicted, color='#ad1010', edgecolor='#000000', label=r"ExtraTreesRegressor - R$^2$=" + "{:.2f}".format(r2) + " - RMSE="+ "{:.0f}".format(rmse) +" K") 
ax.legend()
ax.axis('scaled')
ax.set_xlabel('Expected Temperature values [K]')
ax.set_ylabel('Predicted Temperature values [K]')
   
        

