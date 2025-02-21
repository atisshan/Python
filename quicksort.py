

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: An array with 0 or 1 elements is already sorted.

    pivot = arr[0]  # Choose the pivot (in this case, the first element).
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]

    # Recursively sort the sub-arrays and combine them.
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Example usage:
unsorted_array = [3, 6, 8, 10, 1, 2, 1]
sorted_array = quick_sort(unsorted_array)
print(sorted_array)