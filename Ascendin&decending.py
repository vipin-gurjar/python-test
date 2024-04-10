def ascending_order(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def descending_order(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

numbers = [5, 2, 8, 1, 6, 7, 10, 3]
print("Original List:", numbers)

ascending_result = ascending_order(numbers.copy())
print("Ascending Order:", ascending_result)

descending_result = descending_order(numbers.copy())
print("Descending Order:", descending_result)
