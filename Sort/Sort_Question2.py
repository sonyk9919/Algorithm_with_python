n = int(input())

arr = []
for i in range(n):
    n, m = input().split(" ")
    arr.append((n, int(m)))

arr = sorted(arr, key=lambda s: s[1])
for i in arr:
    print(i[0], end=" ")

