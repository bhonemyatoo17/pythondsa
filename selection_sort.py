def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]

arr = [2,32,4,3,23,12,43,54,3,2]
selection_sort(arr)
print(arr)