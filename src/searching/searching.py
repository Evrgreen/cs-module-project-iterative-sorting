def linear_search(arr, target):
    # Your code here
    for index, item in enumerate(arr):
        if item == target:
            return index

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        middle = low + (high - low) // 2
        middle_value = arr[middle]
        if middle_value == target:
            return middle
        elif middle_value < target:
            low = middle + 1
        else:
            high = middle - 1
    # Element is not present in the array
    return -1
