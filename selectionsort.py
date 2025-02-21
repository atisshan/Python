arr = [4,7,24,5,13]
for i in range(0, len(arr) - 1):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
print(arr)


