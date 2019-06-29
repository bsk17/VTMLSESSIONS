# 1-D is called series
# 2-D is called DataFrame
# 3-D is called Panel

import pandas as pd
import matplotlib.pyplot as plot


# creating 1D
# list1 = [10, 20, 30, 40, 50]
# data1 = pd.Series(list1)
# print(data1)
#
# # output will be this it will also show the index of series
# # 0    10
# # 1    20
# # 2    30
# # 3    40
# # 4    50
#
# print(data1.mean())
# print(data1.std())
# print(data1.median())
# # 30.0
# # 15.811388300841896
# # 30.0

# creating 2D
data2 = pd.DataFrame(
    {'Name': ['Dhoni', 'Virat', 'Rohit', 'Dhawan', 'Chahal'],
     'Match': [330, 305, 270, 149, 440],
     'Run': [10502, 10000, 9000, 8000, 100],
     'Century': [12, 42, 19, 16, 50]}
)


# print(data2)
#      Name  Match    Run  Century
# 0   Dhoni    330  10502       12
# 1   Virat    305  10000       42
# 2   Rohit    270   9000       19
# 3  Dhawan    149   8000       16
# 4  Chahal    440    100       50


# print("SHAPE:", data2.shape)
# SHAPE: (5, 4)

# print("Describe:", data2.describe())
# Describe:             Match           Run    Century
# count    5.000000      5.000000   5.000000
# mean   298.800000   7520.400000  27.800000
# std    105.141333   4257.931517  17.035258
# min    149.000000    100.000000  12.000000
# 25%    270.000000   8000.000000  16.000000
# 50%    305.000000   9000.000000  19.000000
# 75%    330.000000  10000.000000  42.000000
# max    440.000000  10502.000000  50.000000

# print(data2.head(2))
#     Name  Match    Run  Century
# 0  Dhoni    330  10502       12
# 1  Virat    305  10000       42

# to add an attribute
# data2["Six"] = [200, 160, 230, 100, 1]
# print(data2)
#
# print("*"*90)
#
# print(data2.sort_values('Name'))
#
# print("*"*90)
#
# del data2["Century"]
# print(data2)

# axis is one for column and zero for row accordingly we give the values

# data2 = data2.drop(axis=1, columns='Century')
# data2 = data2.drop(axis=0, index=1)
print(data2)
# print(data2.iloc[:, 1:2])

# to save into csv file (comma seperated value file)
data2.to_csv("Cricket.csv", index=None)
print("Data Uploaded")


data = pd.read_csv("Cricket.csv")
print(data)
print("Data Imported")

plot.scatter(data['Match'], data['Century'])
plot.plot(data['Match'], data['Century'])
plot.show()
