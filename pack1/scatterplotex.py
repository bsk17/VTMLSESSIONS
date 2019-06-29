import matplotlib.pyplot as plot

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
y2 = [10, 20, 30, 40, 50]

plot.xlabel("Number")
plot.ylabel("Square")
plot.scatter(x, y)
plot.scatter(x, y2, marker="x")
plot.show()
