def bubble_sort(arr):
    n = len(arr)
    for pass_num in range(n - 1):
        swapped = False
        for i in range(n - 1 - pass_num):  # key optimization
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i] #python swap syntax
                swapped = True
        if not swapped:
            break

arr = [2, 3, 5, 6, 7, 2, 6, 3, 6]
bubble_sort(arr)
print(arr) #only print the arr, not the function