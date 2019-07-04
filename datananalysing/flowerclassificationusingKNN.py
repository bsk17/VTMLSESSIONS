# to classify an input into a class we calculate the distance between the nearest neighbour
# the k specifies how many nearest neighbour we want to compare with

from pandas import read_csv
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

filename = 'IRIS.csv'
dataframe = read_csv(filename)

X = dataframe.iloc[:, :4].values
Y = dataframe.iloc[:, 4].values



# labelencoder_obj = LabelEncoder()
# Y = labelencoder_obj.fit_transform(Y)
#
# onehotencoder_obj = OneHotEncoder(categorical_features=[0])
# Y = onehotencoder_obj.fit_transform(Y).toarray()
#
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=7)

model = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
model.fit(X_train, Y_train)

y_pred = model.predict([[5.1,3.5,1.4,0.2]])
#
# cm = confusion_matrix(Y_test, y_pred)
# print(cm)
print(y_pred)
