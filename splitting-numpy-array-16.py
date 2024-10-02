import numpy as np

# arr = np.array([1, 2, 3,4,5, 6])
# newarr = np.array_split(arr, 6)
# print(newarr)

#split into array


# arr = np.array([[1,2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
# newarr = np.array_split(arr, 7)

# print(newarr)
# arr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where((arr % 2) != 0)
# print(x)


#search sorted
# arr = np.array([6, 8, 9 ,11])
# x = np.searchsorted(arr, 14)
# print(x)

#search from leftside
# arr = np.array([6,7, 8, 9 ])
# x = np.searchsorted(arr, 10, side="left")
# print(x)

#sort method
# arr = np.array([3,2,0,1])
# print(np.sort(arr)[::-1])

# arr = np.array(['banana', 'cherry', 'apple'])
# print(np.sort(arr))

arr = np.array([41, 42, 43, 44, 46, 49, 52, 55])

#Create an empty list
filter_arr = []
#go through each element in arr
for element in arr:
    #if the element is higher than 42, set the value to True, other False:
    if element % 2 == 0: 
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)