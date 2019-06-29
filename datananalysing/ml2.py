
import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import Binarizer
import numpy

dataset = pd.read_csv("data.csv")
print(dataset)
print("------------------------------------------------")



# 1. Load the data and separate dependent(output = y) and independent(input = x) data
x = dataset.iloc[:, :-1].values  # 3rd column tak input hai to usko alag rkho
y = dataset.iloc[:, -1].values   # last column output hai to usko alag rkho

print("------------------------------------------------")
print(x)
print("------------------------------------------------")
print(y)





# 2. Manage missing values by putting mean values
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])
print("After Managing missing values")
print("------------------------------------------------")
print(x)





# 3. Encode Categorical data (kuch bhi string nhi hoga sab numerical format me hoga)
labelencoder_obj = LabelEncoder()
x[:, 0] = labelencoder_obj.fit_transform(x[:, 0])
print("After Encoding X[Country]")
print("------------------------------------------------")
print(x)


# first we convert to some numerical data using label_encoder then using one_hot for readable encoding
onehotencoder_obj = OneHotEncoder(categorical_features=[0])
x = onehotencoder_obj.fit_transform(x).toarray()
print("------------------------------------------------")

# for pretty look and easy calculation we convert to numpy
x = numpy.array(x, dtype=int)
print(x)


# transform y which contains only 1 column
y = labelencoder_obj.fit_transform(y)
print("------------------------------------------------")
print("After Encoding Y[Purchase]")
print(y)

# 4. Splitting to Training and testing the data
# we test 0.3 meaning 30% data and 70% for training
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
print("TRAINING DATA - \n", x_train)
print("------------------------------------------------")
print("Testing Data - \n", x_test)
print("------------------------------------------------")
print("Training Result - \n", y_train)
print("------------------------------------------------")
print("Testing Result - \n", y_test)
print("------------------------------------------------")




# 5. Feature Scaling
# ways to scale a feature
# 5.a Rescale Data
# 5.b Standardize data
# 5.c Normalized data
# 5.d Binarize data

# Rescaling of Data means Transform features by scaling each features to given range
print("After freature Scaling")
scaler = MinMaxScaler(feature_range=(-1, 1))
rescaled = scaler.fit_transform(x)
print(rescaled)
print("------------------------------------------------")

# standardize data has a formula this method is basically used in
# x(stand) = x-mean(x)/ standarddeviation(x)
print("After Standardized Scaling")
scaler2 = StandardScaler()
rescaled2 = scaler2.fit_transform(x)
print(rescaled2)
print("------------------------------------------------")

# normalized data  has a formula x(norm) = (x-x(min))/(max(x)-min(x))
# used in kNearest Neighbour algorithm which is used in sparse data
print("After Normalized data")
scaler3 = Normalizer()
rescaled3 = scaler3.fit_transform(x)
print(rescaled3)
print("------------------------------------------------")

# binarized data all values above the threshhold are marked 1 and below are marked 0
# used for probabilities
print("After Binarizing data")
scaler4 = Binarizer(threshold=2.0)
rescaled4 = scaler4.fit_transform(x)
print(rescaled4)
print("------------------------------------------------")



# 6. Feature Selection
# it is also known as variable creation
# performance depend upon - Choice of algorithm, feature selection,
# feature creation, model creation and selection
# it is of three types
# 6.a Filter Method (individually evaluated)
# 6.b Wrapper Method (jointly evaluated)
# 6.b.1 Subset Selection
# 6.b.2 Forward Selection
# 6.b.3 Backward Selection
# 6.c Embedded Method (inbuilt methods)

#  correlation techniques
# Univariate Selection
# Recursive Feature Selection
# Principle Component Analysis
# Feature Importanat Selection
# we have to care of overfitting and underfitting

# first we need to find the correlation

# feature selection is showed in correlation.py
