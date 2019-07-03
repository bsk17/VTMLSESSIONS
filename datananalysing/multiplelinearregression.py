

# scoringmethod = 'neg_mean_absolute_error'
# from pandas import read_csv
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import cross_val_score
#
# # housing waale file m 14 columns hai jisme se 13 hmare input hai and last waala output
# filename = 'housing2.csv'
# dataframe = read_csv(filename)
# array = dataframe.values
#
# # splitting into inout and output
# X = array[:, 0:13]
# Y = array[:, 13]
#
# # splitting into test and train
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=7)
#
# model = LinearRegression()  # model bnao
# model.fit(X_train, Y_train)  # model m train data daalo
# predictedY = model.predict(X)  # model se output predict kro aur ek array mai daal do
#
# scoringmethod = 'neg_mean_absolute_error'
# results = cross_val_score(model, X_test, Y_test, scoring=scoringmethod)
# print("MAE : %.3f (%.3f)" % (results.mean(), results.std()))
#
# med_val = model.predict([[0.11747, 12.50, 7.870, 0, 0.5240, 6.0090, 82.90, 6.2267, 5, 311.0, 15.20, 396.90,
#                           13.27]])  # 15 saal baad kitta hoga salary ye predict krega
# print("Median Value :", med_val)




# scoringmethod = 'neg_mean_squared_error'
# from pandas import read_csv
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import cross_val_score
#
# # housing waale file m 14 columns hai jisme se 13 hmare input hai and last waala output
# filename = 'housing2.csv'
# dataframe = read_csv(filename)
# array = dataframe.values
#
# # splitting into inout and output
# X = array[:, 0:13]
# Y = array[:, 13]
#
# # splitting into test and train
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=7)
#
# model = LinearRegression()  # model bnao
# model.fit(X_train, Y_train)  # model m train data daalo
# predictedY = model.predict(X)  # model se output predict kro aur ek array mai daal do
#
# scoringmethod = 'neg_mean_squared_error'
# results = cross_val_score(model, X_test, Y_test, scoring=scoringmethod)
# print("MAE : %.3f (%.3f)" % (results.mean(), results.std()))
#
# med_val = model.predict([[0.11747, 12.50, 7.870, 0, 0.5240, 6.0090, 82.90, 6.2267, 5, 311.0, 15.20, 396.90,
#                           13.27]])  # 15 saal baad kitta hoga salary ye predict krega
# print("Median Value :", med_val)




# scoringmethod = 'r2'
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

# housing waale file m 14 columns hai jisme se 13 hmare input hai and last waala output
filename = 'housing2.csv'
dataframe = read_csv(filename)
array = dataframe.values

# splitting into inout and output
X = array[:, 0:13]
Y = array[:, 13]

# splitting into test and train
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=7)

model = LinearRegression()  # model bnao
model.fit(X_train, Y_train)  # model m train data daalo
predictedY = model.predict(X)  # model se output predict kro aur ek array mai daal do

scoringmethod = 'r2'
results = cross_val_score(model, X_test, Y_test, scoring=scoringmethod)
print("MAE : %.3f (%.3f)" % (results.mean(), results.std()))

med_val = model.predict([[0.11747, 12.50, 7.870, 0, 0.5240, 6.0090, 82.90, 6.2267, 5, 311.0, 15.20, 396.90,
                          13.27]])  # 15 saal baad kitta hoga salary ye predict krega
print("Median Value :", med_val)