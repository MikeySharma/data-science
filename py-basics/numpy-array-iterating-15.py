import numpy as np

# arr = np.array([[[1,2,3], [4,5,6]], [[7, 8, 9], [10, 11, 12]]])

# for x in np.nditer(arr):
#     print(x)
    
    
#joining numpy as array

# arr1 = np.array([1,2, 3])
# arr2 = np.array([4,5,6])
# arr = np.concatenate((arr1, arr2))
# print(arr)

# arr1 = np.array([[1,2], [3,4]])
# arr2 = np.array([[5,6], [7,8]])

# arr = np.stack((arr1, arr2), axis=0)
# print(arr)

#Joining Arrays using stack functions

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.dstack((arr1, arr2))
print(arr)