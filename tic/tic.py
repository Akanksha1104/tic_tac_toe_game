import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')

data=pd.read_csv('tic-tac-toe.data.csv')

data.head()

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score

# Positive = 1; Negative = 0;
data['Class'] = data['Class'].replace('positive', 1)
data['Class'] = data['Class'].replace('negative', 0)

# x = 1; b = 0; o = -1;
data = data.replace(('x'), 1)
data = data.replace(('b'), 0)
data = data.replace(('o'), -1)

y = data['Class']
x = data.drop('Class', axis = 1)

X_train,X_test,Y_train,Y_test= train_test_split(x,y, test_size=0.2,random_state=0)

#  KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5)


classifier.fit(X_train, Y_train)
y_pred = classifier.predict(X_test)

# Result
print(classification_report(Y_test, y_pred))

input_data = (-1,-1,1,1,1,-1,-1,1,1)


# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)


# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = classifier.predict(input_data_reshaped)
print(prediction)

import pickle

filename = 'model.pkl'
pickle.dump(classifier, open(filename, 'wb'))


# loading the saved model
loaded_model = pickle.load(open('model.pkl', 'rb'))

input_data = (1,1,1,1,-1,-1,1,-1,-1)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)


# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('Negative')
else:
  print('Positive')