# evaluating means to find the accuracy of the model
# there are many ways to find the acuuracy of the model
# methods of finding accuracy - Classification Accuracy, Logarithmic loss,

# classification accuracy
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
# kfold = KFold(n_splits=num_folds, random_state=7)
# scoringMethod = 'accuracy'
# results = cross_val_score(model, x, y, cv=kfold, scoring=scoringMethod)
# print("Accuracy: %.3f (%.3f)" % (results.mean()*100, results.std()*100))





# logarithmic loss
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
# kfold = KFold(n_splits=num_folds, random_state=7)
# scoringMethod = 'neg_log_loss'
# results = cross_val_score(model, x, y, cv=kfold, scoring=scoringMethod)
# print (results)
# print("Accuracy: %.3f (%.3f)" % (results.mean()*100, results.std()*100))






# area under ROC curve (binary classifications problem)
# works on sensitivity and specificity
from pandas import read_csv
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import KFold
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
model = LogisticRegression()
num_folds = 10
kfold = KFold(n_splits=num_folds, random_state=7)
scoringMethod = 'roc_auc'
results = cross_val_score(model, x, y, cv=kfold, scoring=scoringMethod)
print(results)
print("Accuracy: %.3f (%.3f)" % (results.mean()*100, results.std()*100))





# Confusion matrix (this is an actual demo program)
# from pandas import read_csv
# from sklearn.ensemble import ExtraTreesClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import confusion_matrix
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
# test_size = 0.33
# seed = 7
# x_train, x_test, y_train, y_test = \
#     train_test_split(x, y, test_size=test_size, random_state=seed)
# model = LogisticRegression()
# model.fit(x_train, y_train)
# predicted = model.predict(x_test)  # this function is used to
#
# matrix = confusion_matrix(y_test, predicted)
# print(matrix)
