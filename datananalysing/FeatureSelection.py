import pandas as pd
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import warnings

warnings.filterwarnings("ignore")

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names=hnames)

array = dataframe.values
set_printoptions(precision=3)
x = array[:, 0:8]
y = array[:, 8]

print(x[0:20, :])
print("-"*80)
test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(x, y)  # this will compare 1-7 column to 8th column
set_printoptions(precision=3)
print(fit.scores_)  # [ 111.52  1411.887   17.605   53.108 2175.565  127.669    5.393  181.304]
# the above list shows the score of each column for selection based on output matrix (observe the top 4)
print("-"*80)
features = fit.transform(x)  # this will select the top 4 columns based on score for selection as k=4
print(features[0:20, :])
print("-"*80)
