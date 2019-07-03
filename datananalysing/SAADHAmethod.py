import numpy as np

x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([3,5,7,9,11,13,15,17,19,21])
n = np.size(x)
sumofx = np.sum(x)
sumofy = np.sum(y)
sumofxy = np.sum(x*y)
sumofxsquare = np.sum(x*x)

slope = (n*sumofxy-sumofx*sumofy)/(n*sumofxsquare-sumofx*sumofx)
intercept = (sumofy*sumofxsquare-sumofx*sumofxy)/(n*sumofxsquare-sumofx*sumofx)

print("slope :", slope)
print("Intercept : ", intercept)