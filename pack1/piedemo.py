import matplotlib.pyplot as plot

# sub = ['Maths', 'English', 'Hindi', 'Science', 'Sanskrit']
# marks = [75, 34, 80, 95, 99]
# color = ['r', 'g', 'b', 'k', 'c']
# plot.pie(marks, labels=sub, colors=color, autopct="%3.2f")
# plot.show()


# for stack plot
people = ['A', 'B', 'C', 'D']
sleeping = [6, 8, 5, 10]
reading = [5, 6, 9, 2]
playing = [7, 6, 3, 5]
masti = [6, 4, 7, 7]

plot.stackplot(people, sleeping, reading, playing, masti)
plot.show()
