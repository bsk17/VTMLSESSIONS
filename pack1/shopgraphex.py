# create a graph for shop

import matplotlib.pyplot as plt
import numpy as np

sales1 = [1000, 1200, 300, 500, 600,
         700, 800, 300, 200, 1000, 1100, 1050]

sales2 = [1200, 1400, 100, 400, 500,
          1000, 600, 500, 1000, 1200, 1000, 1055]

months = ["jan", "feb", "mar", "apr", "may",
          "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
x1 = np.arange(1, 13)


plt.bar(x1-0.2, sales1, color="blue", width=0.5, label="C1")
plt.bar(x1+0.2, sales2, color="red", width=0.5, label="C2")
plt.xticks(x1)
plt.yticks(range(0, 1500, 100))
plt.legend()
plt.show()
