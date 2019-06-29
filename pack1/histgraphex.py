import matplotlib.pyplot as plot
import numpy as np

marks = [55, 62, 63, 63, 57, 71, 54, 45, 92, 77, 58, 63, 67, 46]
x = np.arange(10, 101, 10)
plot.hist(marks, x)
plot.show()
