from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plot
from sklearn.preprocessing import PolynomialFeatures

filename = 'Position_Salaries.csv'
dataframe = read_csv(filename)
array = dataframe.values

# splitting into input and output
X = array[:, 1:2]
Y = array[:, 2]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=7)

poly_reg = PolynomialFeatures(degree=6)
X_Poly = poly_reg.fit_transform(X)
poly_reg.fit(X_Poly, Y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_Poly, Y)

plot.scatter(X, Y, color='red')  # pehle simple data plot krenge
plot.plot(X, lin_reg_2.predict(X_Poly), color="blue")
plot.title("truth or Bluff (Polynomial Bluff)")
plot.xlabel("Poisiton Level")
plot.ylabel("Salary")
plot.show()

