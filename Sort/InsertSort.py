arr = [3, 4, 1, 5, 2, 6, 0]
n = len(arr)

for i in range(1, n):
    for j in range(i, 0, -1):
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else:
            break

print(arr)