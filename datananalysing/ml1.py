# the steps needed to do before processing the data
# we will use datafiles externally


# import csv
#
# fp =open("indians-diabetes.data.csv", "r")  # usually how we open
# reader = csv.reader(fp, delimiter=",")  # for csv file content
# print(type(reader))
# lines = list(reader)  # converting to list
# print("NO of rows", len(lines))
#
# for i in lines:  # for single lines in lists
#     print(i)


# using numpy
# import numpy
#
# fp = open("indians-diabetes.data.csv", "r")
# data = numpy.loadtxt(fp, delimiter=",")
#
# for i in data:
#     print(i)


# using urllib and numpy (for servers)
# import numpy
# import urllib.request
#
# web_path = urllib.request.urlopen("https://goo.gl/QnHW4g")
# dataset = numpy.genfromtxt(web_path, delimiter=",")
#
# for lines in dataset:
#     print(lines)

# using pandas from local file
# import pandas
# hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
# file = pandas.read_csv("indians-diabetes.data.csv", names=hnames)
# print(file)

# using pandas and urllib
import pandas
import urllib.request

nameheadings = ['length', 'width', 'length1', 'width1', 'class']
web_path = urllib.request.urlopen("https://goo.gl/QnHW4g")
dataframe = pandas.read_csv(web_path, names=nameheadings)

print(dataframe)
