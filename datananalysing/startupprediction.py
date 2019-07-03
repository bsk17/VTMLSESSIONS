from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# housing waale file m 14 columns hai jisme se 13 hmare input hai and last waala output
filename = '50_Startups.csv'
dataframe = read_csv(filename)
array = dataframe.values

# splitting into input and output
X = array[:, 0:4]
Y = array[:, 4]

labelencoder_obj = LabelEncoder()
X[:, 3] = labelencoder_obj.fit_transform(X[:, 3])

onehotencoder_obj = OneHotEncoder(categorical_features=[3])
X = onehotencoder_obj.fit_transform(X).toarray()
print(X)
# x = numpy.array(X, dtype=int)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=7)
model = LinearRegression()
model.fit(X_train, Y_train)
predictedY = model.predict(X)

profit = model.predict([[0, 0, 1, 165349.2, 136897.8, 471784.1]])
print("Profit : ", profit)
