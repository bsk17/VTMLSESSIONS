# RFE works by recursively eliminating attributes and building a model on those attributes that remain

# pehle saare attributes ko leke model bnao aur uske baad ek ek ko remove kro compare

from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
import warnings

warnings.filterwarnings("ignore")
filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=hnames)
array = dataframe.values
print(array[:20, :])
x = array[:, 0:8]
y = array[:, 8]
model = LogisticRegression()
rfe = RFE(model, 4)
fit = rfe.fit(x, y)
result = fit.transform(x)
print("-"*70)
print("Num Featurs = ", fit.n_features_)
print("-"*70)
print("Selected Features = ", fit.support_)
print("-"*70)
print("Feature Ranking = ", fit.ranking_)
print("-"*70)
print(result[:20, :])
