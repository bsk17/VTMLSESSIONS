import matplotlib.pyplot as plot
import numpy as np

deg = [0, 30, 45, 60, 90, 120, 180]
val = []

for i in deg:
    rad = np.radians(i)
    val.append(np.sin(rad))

plot.xticks(range(0, 180, 10))
plot.plot(deg, val)
plot.show()