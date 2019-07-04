# this works on probability
# when we have to check about the probability of some result we will use this method

#
from pandas import read_csv
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB

filename = 'Social_Network_Ads.csv'
dataframe = read_csv(filename)

X = dataframe.iloc[:, [2,3]].values
Y = dataframe.iloc[:, 4].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=7)


sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

model = GaussianNB()
model.fit(X_train, Y_train)

y_pred = model.predict(X_test)

cm = confusion_matrix(Y_test, y_pred)
print(cm)