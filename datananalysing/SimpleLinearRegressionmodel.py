# Simple Linear Regression Model
# y= mx+c



# example 1
# from pandas import read_csv
# import matplotlib.pyplot as plot
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
#
# filename = 'Salary_Data.csv'
# dataframe = read_csv(filename)
# array = dataframe.values
#
# # splitting into inout and output
# X = array[:, 0:1]
# Y = array[:, 1]
#
# # splitting into test and train
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=7)
#
# model = LinearRegression()  # model bnao
# model.fit(X_train, Y_train)  # model m train data daalo
#
# predictedY = model.predict(X)  # model se output predict kro
# year = eval(input("Enter the experience in years"))
# predictedsal = model.predict([[year]])  # 15 saal baad kitta hoga salary ye predict krega
# print("Predicted Salary :", predictedsal)
#
# plot.scatter(X, Y, color='red')  # pehle simple data plot krenge
# plot.xlabel("Years")
# plot.ylabel("Salary")
# plot.yticks(range(10000, 150000, 10000))
# plot.xticks(range(0, 15, 1))
# plot.plot(X, predictedY, color="b")  # predicted data plot krenge
# plot.show()


# example 2
from pandas import read_csv
import matplotlib.pyplot as plot
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

filename = 'mine.csv'
dataframe = read_csv(filename)
array = dataframe.values

# splitting into inout and output
X = array[:, 0:1]
Y = array[:, 1]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=7)

model = LinearRegression()  # model bnao
model.fit(X_train, Y_train)  # model m train data daalo
print("Slope : ", model.coef_)  # slope of the graph
print("Intercept : ", model.intercept_)  # intercept of graph

predictedY = model.predict(X)  # model se output predict kro
num = eval(input("Enter the number"))
predictednum = model.predict([[num]])  # 15 saal baad kitta hoga salary ye predict krega
print("Predicted NUMBER :", predictednum)
