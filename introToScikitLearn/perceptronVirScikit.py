# Training a perceptron via scikit-learn
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

import sys
sys.path.append('../Utilities/')
import printDecisionRegion as printDR
import sklearnReadData as skRead
import matplotlib.pyplot as plt

print('Training a perceptron via scikit-learn')

# Use utility API to read data out of sklearn library
dataSet = skRead.sklearnReadIris()
X_train_std = dataSet['X_train_std']
y_train = dataSet['y_train']
X_test_std = dataSet['X_test_std']
y_test = dataSet['y_test']

# Now use perceptron to train the Train dataset and predict against 
# Test dataset to see accuracy
ppn = Perceptron(n_iter = 40, eta0 = 0.1, random_state = 0)
ppn.fit(X_train_std, y_train)
y_pred = ppn.predict(X_test_std)
print('# of misclassfied samples ', (y_test != y_pred).sum())
print('Accuracy Score ', accuracy_score(y_test, y_pred))

# Print decision region and all samples
X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))
printDR.printDecisionRegionWithTestIdx(X = X_combined_std, y = y_combined, 
	                                   classifier = ppn, test_idx = range(105, 150))
plt.xlabel('petal length [Standarized]')
plt.ylabel('petal width [Standarized]')
plt.legend(loc = 'upper left')
plt.show()