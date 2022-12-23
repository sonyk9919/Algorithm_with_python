n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = max(arr)
result = 0
while left <= right:
    mid = (left + right) // 2
    remain = [i - mid for i in arr if i - mid >= 0]
    total = sum(remain)
    if total < m:
        right = mid - 1
    else:
        left = mid + 1
        result = mid

print(result)