#Write a function that takes a list and returns the list in reverse order.
import numpy as np

def reverse_list(array):
    return array[::-1]

arr = np.array([1,2,3,4,5])

print(reverse_list(arr))

# Write a function to return the sum of all elements in a given list.
def sum_of_list(array):
    total=0
    for item in array:
        total += item
    print("Sum of items in list is :", total)

sum_of_list(arr)

#Write a function that returns the maximum element from a list.
def find_max(array):
    max = np.array(array).max()
    return max
print("Max of given list is:", find_max(arr))

#Write a function to return the minimum element from a list.

def find_min(array):
    min = np.array(array).min()
    return min
print("Min of given list is:", find_min(arr))

#Write a function to find the second largest number in a list.
def second_largest(array):
    return np.sort(array)[len(arr) - 2]
    
print("Second largest number is:", second_largest(arr))

#Write a function to remove duplicate elements from a list.
def remove_duplicate(array):
    return np.array(list(set(array)))

dup_arr = np.array(['apple', 'orange', 'apple'])
print("With duplicate :", dup_arr, "Without duplicate: ", remove_duplicate(dup_arr))