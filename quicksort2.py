def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    less=[]
    great=[]
    pivot=arr[0]
    
    for x in arr[1: ]:
        if x <= pivot:
            less.append(x)

        else:
            great.append(x)
    return quick_sort(less) + [pivot] + quick_sort(great)


arr=[3, 6, 8, 10, 2, 1, 1]
sort=quick_sort(arr)
print(sort)
