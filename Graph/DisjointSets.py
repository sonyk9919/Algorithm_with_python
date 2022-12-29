import sys

input = sys.stdin.readline

def findParents(parents, x):
    if parents[x] != x:
        parents[x] = findParents(parents, parents[x])
    return parents[x]

def unionParents(parents, a, b):
    a = findParents(parents, a)
    b = findParents(parents, b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a
    

v, e = map(int, input().split())

parents = [i for i in range(v + 1)]

for i in range(e):
    a, b = map(int, input().split())
    unionParents(parents, a, b)

# parents Array를 한번 돌면서 아직 parents가 변경되지 않은 값들을 refresh한다.
# for i in range(1, v + 1):
#     findParents(parents, i)

for i in range(1, v + 1):
    print(parents[i], end=" ")

print()
