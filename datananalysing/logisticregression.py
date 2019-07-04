from pandas import read_csv
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

filename = 'Social_Network_Ads.csv'
dataframe = read_csv(filename)

X = dataframe.iloc[:, [2,3]].values
Y = dataframe.iloc[:, 4].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=7)


sc = StandardScaler()
Xtrain = sc.fit_transform(X_train)
Xtest = sc.transform(X_test)


model = LogisticRegression(random_state=0)
model.fit(Xtrain, Y_train)
y_pred = model.predict(Xtest)

cm = confusion_matrix(Y_test, y_pred)
print(cm)

