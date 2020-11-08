def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if(arr[i] == target):
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high=len(arr) - 1
    mid = 0

    while low <= high:
        mid = (low+high)//2

        if(arr[mid] < target):
            low = mid+1
        elif(arr[mid]>target):
            high=mid-1
        else:
            return mid
    return -1  # not found
