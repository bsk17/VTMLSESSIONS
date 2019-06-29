import matplotlib.pyplot as plt

plt.figure()

plt.subplot(221)  # indexing of sub plotting
x = [1, 2, 3]
y = [1, 4, 9]
plt.xlabel("X")
plt.ylabel("Square")
plt.plot(x, y, color="red")

plt.subplot(222)
x = [1, 2, 3]
y = [1, 4, 9]
plt.xlabel("X")
plt.ylabel("Square")
plt.scatter(x, y, color="g")

plt.subplot(223)
x = [1, 2, 3]
y = [1, 4, 9]
plt.xlabel("X")
plt.ylabel("Square")
plt.scatter(x, y, color="g", marker="x")

plt.subplot(224)
x = [1, 2, 3]
y = [1, 4, 9]
plt.xlabel("X")
plt.ylabel("Square")
plt.bar(x, y, color="b")

plt.show()
