#arr = list(map(int, input()))
arr = [3, 4, 1, 5, 2, 6, 0]
n = len(arr)

for i in range(n):
    minIndex = i
    for j in range(i, n):
        if arr[minIndex] >= arr[j]:
            minIndex = j
    arr[i], arr[minIndex] = arr[minIndex], arr[i]

print(arr)