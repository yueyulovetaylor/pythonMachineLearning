from perceptronLearning import Perceptron

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print('Implementation of Perceptron Learning')
# Use pandas library to import all data into a framework and 
# tail the last five lines
df = pd.read_csv('iris.data', header = None)

print('Tail last five rows of the dataset')
last5Samples = df.tail(5) 
	# tail(n) api returns the last n rows of the dataframe
print(last5Samples)

# Use the first 100 class labels with 50 1's (Versicolor) and
# -1 (Setaso), also extract the first and third columns

# Data clean and visualization
y = df.iloc[0: 100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
X = df.iloc[0: 100, [0, 2]].values

# Plot red 'o' as Setosa and 'x' as 'Versicolor'
plt.scatter(X[:50, 0], X[0: 50, 1], color = 'red', marker = 'o', label = 'Setaso')
plt.scatter(X[50: 100, 0], X[50: 100, 1], color = 'blue', marker = 'x', label = 'Virginica')
plt.xlabel('sepal length')
plt.ylabel('petal length')
plt.legend(loc='upper left')
print('\nPrint Initial dataset in two dimensions')
plt.show()

# Use perceptron to train the data for classification
ppn = Perceptron(eta = 0.1, n_iter = 10)
ppn.fit(X, y)