import pandas

filename = "indians-diabetes.data.csv"
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(filename, names=hnames)

print(dataframe)
print("*"*80)

corr = dataframe.corr(method='pearson')
print("Correlation \n", corr)
