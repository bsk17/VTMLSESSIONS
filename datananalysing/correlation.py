import pandas
from matplotlib import pyplot as plot

filename = "indians-diabetes.data.csv"
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(filename, names=hnames)

print(dataframe)
# print("*"*80)
#
# corr = dataframe.corr(method='pearson')
# print("Correlation \n", corr)
# # correlation refers to the relation between two variables and how they may or may not
# # change together

# # histogram code for univariate selection
# dataframe.hist()

# density plot
dataframe.plot(kind='density', subplots=True, layout=(3, 3), sharex=False)

plot.show()
