import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

# 2015-11-03 to 2021-08-05

data = pd.read_csv("316140.csv", sep=",")

data = data[["high", "low", "close"]]

predict = "close"  # Label

x = np.array(data.drop([predict], 1))  # Features (REMOVE G3 FROM LIST) --> Does not know answer
y = np.array(data[predict])  # Label (JUST THE G3 FROM ENTIRE LIST) --> Answer Key

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)

acc = linear.score(x_test, y_test)
print(acc)

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])


