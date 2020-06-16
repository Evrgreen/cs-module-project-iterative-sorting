# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        '''
        loop through the array
        compare smallest_index to the value of the next index
        if next index is smaller set smallest_index to next index value
        end of the loop set the current index to be the smallest index
        '''
        for next_index in range(i, len(arr)-1):
            if arr[smallest_index] > arr[next_index+1]:
                smallest_index = next_index+1
                # print(smallest_index)
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

        # TO-DO: swap
        # Your code here

    return arr


print(selection_sort([3, 4, 5, 1, 2]))
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    length = len(arr)
    for item in range(length-1):
        for index in range(0, length-item-1):
            if arr[index] > arr[index+1]:
                arr[index], arr[index+1] = arr[index+1], arr[index]


# Your code here
# loop through array
# compare left item to right item
# if left is larger than right swap them

    return arr


print(bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the
buckets.

What is the time and space complexity of the counting sort algorithm?
'''



