# sometimes we have to seperate data based on conditions

# different methods of separation are
# simple train and test separation, k fold Cross Validation, Leave one out cross validation,
# Repeated random test-train separation
# 1. train_test_separate() - we specify some percent of data to train and test ye hum kar chuke hai
# 2. K-fold - divide the data into parts and from that parts take training and testing data
# 3. Leave One out cross validation- it is like k fold but size of k is 1
# 4. Repeated random test - similar to first one but repeated



# k fold method
# from pandas import read_csv
# from sklearn.ensemble import ExtraTreesClassifier
# from sklearn.model_selection import KFold
# from sklearn.model_selection import cross_val_score
# from sklearn.linear_model import LogisticRegression
# import warnings
#
# warnings.filterwarnings("ignore")
# filename = 'indians-diabetes.data.csv'
# hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
# dataframe = read_csv(filename, names=hnames)
# array = dataframe.values
# x = array[:, 0:8]
# y = array[:, 8]
# model = LogisticRegression()
# num_folds = 10
# kfold = KFold(n_splits=num_folds)
# results = cross_val_score(model, x, y, cv=kfold)
# print("Results  : ", results)
# print("Accuracy: %.3f%%" % (results.mean()*100.0))
# print("Std.Deviation: %.3f" % (results.std()*100.0))





# # Leave one out
# from pandas import read_csv
# from sklearn.model_selection import LeaveOneOut
# from sklearn.model_selection import cross_val_score
# from sklearn.linear_model import LogisticRegression
# import warnings
#
# warnings.filterwarnings("ignore")
# filename = 'indians-diabetes.data.csv'
# hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
# dataframe = read_csv(filename, names=hnames)
# array = dataframe.values
# x = array[:, 0:8]
# y = array[:, 8]
# loocv = LeaveOneOut()
# model =  LogisticRegression()
# results = cross_val_score(model, x, y, cv=loocv)
# print("Results : " , results)
# print("-"*80)
# print("Result size : ", results.size)
# print("-"*80)
# print("Sum of positive results : %i" %(results.sum()))
# print("-"*80)
# print("Accuracy : %.2f %%" %(results.sum()*100/results.size))
# print("-"*80)





# repeated random test train
from pandas import read_csv
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
import warnings

warnings.filterwarnings("ignore")
filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=hnames)
array = dataframe.values
x = array[:, 0:8]
y = array[:, 8]
test_size = 0.33
no_of_repetitions = 10
shufflesplit = ShuffleSplit(n_splits=no_of_repetitions, test_size=test_size)
model = LogisticRegression()
results = cross_val_score(model, x, y, cv=shufflesplit)
print(results)
print("-"*80)
print("Accuracy : %.3f" % (results.mean()*100.0))
print("-"*80)
print("Std Deviation = %.3f" % (results.std()*100))
