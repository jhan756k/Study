import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

data = pd.read_csv("student-mat.csv ", sep=";")
# print(data.head())
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"  # Label

x = np.array(data.drop([predict], 1))   # Features (REMOVE G3 FROM LIST) --> Does not know answer
y = np.array(data[predict])     # Label (JUST THE G3 FROM ENTIRE LIST) --> Answer Key

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

# THIS FUNCTION ONLY ALLOCATES DATA (DOESN'T PREDICT)

# Split 10% of data for the x,y test arrays
# Prevents train model from being "overfitted" --> perfectly trained models tend to make big mistakes when data
# goes outside the tolerance even just a little bit.


linear = linear_model.LinearRegression()


linear.fit(x_train, y_train)    # Find best linear function and stores it in "linear"
accuracy = linear.score(x_test, y_test)     # Checks the accuracy using test values to score the "best linear function"
print(accuracy)

print("Coefficient: \n", linear.coef_)
print("Intercept: \n", linear.intercept_)

predictions = linear.predict(x_test)
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

