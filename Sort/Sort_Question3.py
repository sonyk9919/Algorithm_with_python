# n은 원소의 개수, m은 바꿔치기 횟수
n, m = map(int, input().split())

arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

for i in range(m):
    v1, v2 = max(arrB), min(arrA)
    idx1, idx2 = arrB.index(v1), arrA.index(v2)
    if arrA[idx2] < arrB[idx1]:
        arrA[idx2], arrB[idx1] = arrB[idx1], arrA[idx2]
    else:
        break
print(sum(arrA))
