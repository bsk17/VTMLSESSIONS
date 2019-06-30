from pandas import read_csv
from sklearn.ensemble import ExtraTreesClassifier
import warnings

warnings.filterwarnings("ignore")
filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=hnames)
array = dataframe.values
x = array[:, 0:8]
y = array[:, 8
    ]

model = ExtraTreesClassifier()
model.fit(x, y)
scores = model.feature_importances_
# print(x)
# print("-"*80)
print(scores)
