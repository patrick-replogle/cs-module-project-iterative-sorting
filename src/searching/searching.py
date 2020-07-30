import time

arr = []
for i in range(1000000):
    arr.append(i)


def linear_search(arr, target):
    for num in arr:
        if num == target:
            return True
    return -1


print('Linear Search')
linear_start = time.time()
print(linear_search(arr, 9492))
linear_end = time.time()
print(f"Runtime: {linear_end - linear_start}")


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (r + l) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
    return -1


print('Binary Search')
binary_start = time.time()
print(binary_search(arr, 5930))
binary_end = time.time()
print(f"Runtime: {binary_end - binary_start}")
