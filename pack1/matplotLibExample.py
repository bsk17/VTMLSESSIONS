import matplotlib.pyplot as plot

over = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
runsIND = [0, 5, 10, 20, 30, 35, 46, 53, 64, 75, 100]
runsAUS = [23, 26, 26, 34, 45, 12, 24, 67, 78, 89, 100]

plot.title("INDIA BATTING")  # to set title
plot.plot(over, runsIND, color='red', linewidth=5, label="ind")  # first argument x axis second argument y axis
plot.plot(over, runsAUS, color='blue', linewidth=5, label="Aus")
plot.xlabel("OVER")  # to put labels
plot.xticks(over)  # to cover all the elements
plot.ylabel("RUNS")
plot.plot(over[4], runsIND[4], "or")  # or stands for oval red
plot.plot(over[7], runsIND[7], "sr")
plot.yticks(range(0, 105, 5))
plot.grid()  # this will show graphs
plot.legend()
plot.show()
