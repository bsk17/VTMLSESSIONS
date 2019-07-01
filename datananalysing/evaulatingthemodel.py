# evaluating means to find the accuracy of the model
# there are many ways to find the acuuracy of the model


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

