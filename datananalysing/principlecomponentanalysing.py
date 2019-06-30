# pca will convert the data into some other format and then select the best features
# which can be used later on

from pandas import read_csv
from sklearn.decomposition import PCA
filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=hnames)
array = dataframe.values
x = array[:, 0:8]
y = array[:, 8]
print(x)
print("-"*80)
pca = PCA(n_components=3)
x = pca.fit_transform(x)
print(x)
print("-"*80)
explained_variance = pca.explained_variance_ratio_
print(explained_variance)
print("-"*80)
