import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import warnings

warnings.filterwarnings("ignore")

dataset1 = pd.read_csv('train.csv')  # this is the train dataset
dataset2 = pd.read_csv('test.csv')  # this is the test dataset
dataset3 = pd.read_csv('gender_submission.csv')  # this dataset is for y test

X_train = dataset1.iloc[:, [2, 4, 5, 6, 7, 11]].values  # we select the values manually for input
Y_train = dataset1.iloc[:, 1].values  # we select the values manually for input
X_test = dataset2.iloc[:, [1, 3, 4, 5, 6, 10]].values  # we select the values manually for input
Y_test = dataset3.iloc[:, 1].values  # we select the values manually for input

# to fill in the missing values we use the most frequent value from a column
imputer = Imputer(missing_values="NaN", strategy="most_frequent", axis=0)

# we fill the missing values of age in train data
imputer.fit(X_train[:, [2]])
X_train[:, [2]] = imputer.transform(X_train[:, [2]])

# we fill the missing values of test data
imputer.fit(X_test[:, [2]])
X_test[:, [2]] = imputer.transform(X_test[:, [2]])

# to encode gender and embarked from training and testing data
labelencoder_x = LabelEncoder()
X_train[:, 1] = labelencoder_x.fit_transform(X_train[:, 1])
X_train[:, 5] = labelencoder_x.fit_transform(X_train[:, 5])
X_test[:, 1] = labelencoder_x.fit_transform(X_test[:, 1])
X_test[:, 5] = labelencoder_x.fit_transform(X_test[:, 5])

print(X_train)
# we are using logistic regression because it gives an accuracy of 96.6 %
model = LogisticRegression(random_state=0)
model.fit(X_train, Y_train)

# now we will be taking input from the user and encoding them to predict correct input
print("Let us check will you live or die !!!!!!!!!!!!!!!!!!!!!!!!!!!")

pclass = eval(input("Enter your ticket class (between 1-3) : "))
gender = eval(input("Enter the gender (1 for male \t 0 for female) : "))
age = eval(input("Enter your age : "))
sibling = eval(input("Enter number of sibling : "))
parch = eval(input("Enter number of parent/children"))

# we have to convert the embarkment as we have encoded it so here we will decode and send
embarkment = input("Enter the port of embarkment \nS for Southampton \nQ for Queenstown \nC for cherbourg")
if embarkment == 'S':
    embarkment = 2
elif embarkment == 'Q':
    embarkment = 1
else:
    embarkment = 0

survival = model.predict([[pclass, gender, float(age), sibling, parch, embarkment]])

# the survival is in 1 or 0 to make it user friendly we will add it
if survival == 0:
    print("You should not go as you will not survive!")
else:
    print("You are all set to go")
