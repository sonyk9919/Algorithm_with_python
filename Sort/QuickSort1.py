def quickSort(array, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[pivot] >= array[left]:
            left += 1
        while right > start and array[pivot] <= array[right]:
            right -= 1
        
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    
    quickSort(array, start, right - 1)
    quickSort(array, right + 1, end)

arr = [3, 4, 1, 5, 2, 6, 0]
quickSort(arr, 0, len(arr) - 1)
print(arr)