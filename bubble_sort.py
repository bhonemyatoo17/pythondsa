def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i] #python swap code
                swapped = True

arr = [2,3,5,6,7,2,6,3,6]
bubble_sort(arr)
print(arr)  # print the array directly
