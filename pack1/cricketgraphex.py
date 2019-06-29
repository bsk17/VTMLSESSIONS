import matplotlib.pyplot as plot
import numpy as np

overs = np.arange(10, 60, 10)
indBat = [50, 58, 70, 85, 114]
ausBat = [48, 63, 60, 95, 100]

plot.bar(overs-0.5, indBat, color="blue", width=1, label="IND")
plot.bar(overs+0.5, ausBat, color="yellow", width=1, label="AUS")
plot.yticks(range(0, 120, 10))
plot.plot(overs[0]+0.5, ausBat[0]-5, "or", label="WICKET")
plot.plot(overs[0]+0.5, ausBat[0], "or")
plot.plot(overs[1]-0.5, indBat[1], "or")
plot.plot(overs[2]-0.5, indBat[2], "or")
plot.plot(overs[2]-0.5, indBat[2]-5, "or")
plot.plot(overs[2]+0.5, ausBat[2], "or")
plot.plot(overs[2]+0.5, ausBat[2]-5, "or")
plot.plot(overs[2]+0.5, ausBat[2]-10, "or")
plot.plot(overs[4]+0.5, ausBat[4], "or")
plot.plot(overs[4]+0.5, ausBat[4]-5, "or")
plot.plot(overs[4]+0.5, ausBat[4]-10, "or")
plot.grid()
plot.legend()
plot.show()
