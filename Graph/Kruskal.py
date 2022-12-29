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
        parents[b]= a

v, e = map(int, input().split())
parents = [i for i in range(v + 1)]
edges = []
result = 0

for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if findParents(parents, a) != findParents(parents, b):
        unionParents(parents, a, b)
        result += cost

print(result)