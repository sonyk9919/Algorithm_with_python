arr = [3, 4, 1, 5, 2, 6, 0]

def merge(leftArr, rightArr):
    total = []
    left = len(leftArr)
    right = len(rightArr)

    i, j = 0, 0
    while i < left and j < right:
        if leftArr[i] <= rightArr[j]:
            total.append(leftArr[i])
            i += 1
        else:
            total.append(rightArr[j])
            j += 1
    
    if i == left:
        while j < right:
            total.append(rightArr[j])
            j += 1
    elif j == right:
        while i < left:
            total.append(leftArr[i])
            i += 1
    
    return total

def mergeSort(arr, left, right):
    if left == right:
        return [arr[left]]

    mid = (left + right) // 2
    leftArr = mergeSort(arr, left, mid)
    rightArr = mergeSort(arr, mid + 1, right)

    return merge(leftArr, rightArr)

print(mergeSort(arr, 0, len(arr) - 1))