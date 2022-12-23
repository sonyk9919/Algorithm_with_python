def binarySearch(arr, target, left, right):
    if (left > right):
        return -1
    mid = (left + right) // 2
    if (arr[mid] == target):
        return mid
    elif (arr[mid] > target):
        return binarySearch(arr, target, left, mid - 1)
    else:
        return binarySearch(arr, target, mid + 1, right)

target = int(input())
arr = list(map(int, input().split()))
search = binarySearch(arr, target, 0, len(arr) - 1)

if search:
    print("arr[{}]".format(search), arr[search])
else:
    print("Not exist")