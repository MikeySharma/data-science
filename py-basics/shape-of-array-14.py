import numpy as np

# arr = np.array([[1, 2, 3, 4], [5,6,7,8]])
# print(arr.shape)

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(arr.shape)

newarr = arr.reshape(2, 3,2)
print(newarr)