def quickSort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quickSort(left) + [pivot] + quickSort(right)

arr = [3, 4, 1, 5, 2, 6, 0]
print(quickSort(arr))
