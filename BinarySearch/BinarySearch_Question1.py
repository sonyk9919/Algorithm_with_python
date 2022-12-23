def binarySearch2(arr, target, left, right):
    if left > right:
        return False
    mid = (left + right) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return binarySearch2(arr, target, left, mid - 1)
    else:
        return binarySearch2(arr, target, mid + 1, right)

n = int(input())
arrN = list(map(int, input().split()))

m = int(input())
arrM = list(map(int, input().split()))

arrN = sorted(arrN)
for i in arrM:
    if binarySearch2(arrN, i, 0, (len(arrN) - 1)):
        print("yes", end=" ")
    else:
        print("no", end=" ")