arr = [9,10,11,12,13,14,15,16] #assorted array

def binarySearch(arr,target):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binarySearch(arr,12))


