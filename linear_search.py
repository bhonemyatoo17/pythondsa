def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i  # return index immediately when found
    return -1  # return -1 if never found

# Test it
numbers = [1, 2, 35, 324, 63, 34, 23, 43, 53]
result = linear_search(numbers, 63)

if result != -1:
    print(f"Found at index {result}")
else:
    print("Not found")