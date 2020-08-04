import time

arr = []
for i in range(1000000):
    arr.append(i)


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


print('\nLinear Search')
linear_start = time.time()
print('Output: ', linear_search(arr, 94921))
linear_end = time.time()
print(f'Runtime: {linear_end - linear_start}\n')


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1
    return -1


print('Binary Search')
binary_start = time.time()
print('Output: ', binary_search(arr, 94921))
binary_end = time.time()
print(f'Runtime: {binary_end - binary_start}\n')
