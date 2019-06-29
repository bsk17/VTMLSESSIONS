import numpy as np
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
#
# # adding element wise
# # data type of lists should be numpy.ndarray
# arr1 = np.array(list1)
# print(arr1, type(arr1))
#
# arr2 = np.array(list2)
# print(arr2, type(arr2))
#
# # we can perform any mathematical expression
# print(arr1 + arr2)
#
# print(arr2.dtype)
# # if we convert any one element to different type all the
# # elements will get converted as it process array


# list3 = [1, 2, 3, 4, 5]
# list4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# list5 = [[1, 2, 3], [4, 5, 6, 7], [1, 2]]  # this is zig zag array
# arr3 = np.array(list3)
# arr4 = np.array(list4)
# arr5 = np.array(list5)
# print(arr3)
# print(arr4)
# print(arr5)
#
#
# # Inbuilt attributes of numpy

# # for data type
# print(arr3.dtype)
# print(arr4.dtype)
# print(arr5.dtype)
#
# # shape gives the dimensions elements of array
# print(arr3.shape)
# print(arr4.shape)
# print(arr5.shape)
#
# # dimension
# print(arr3.ndim)
# print(arr4.ndim)
# print(arr5.ndim)
#
# # how much size one element will take
# print(arr3.itemsize)
# print(arr4.itemsize)
# print(arr5.itemsize)
#
#
# # special functions
# print(arr3.sort())
# print(arr3.min())
# print(arr3.max())
# print(arr3.sum())
# print(arr3.mean())
# print(arr3.std())


# list6 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# list7 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
#
# arr6 = np.array(list6)
# arr7 = np.array(list7)
#
# print(arr6)
# print(arr6.dot(arr7))  # to multiply array
# print(arr6.transpose())
# print(np.invert(arr6))

# numpy array creation method
arr1 = np.arange(10)
print(arr1)
arr2 = np.arange(10, 100, 5)
print(arr2)
arr3 = np.eye(3, 3, dtype=int)  # identity matrix
print(arr3)
arr4 = np.zeros((3, 3), dtype=int)  # zero matrix
print(arr4)
arr5 = np.ones((3, 3), dtype=int)
print(arr5)
arr6 = np.ones((3, 3), dtype=int) * 5
print(arr6)
