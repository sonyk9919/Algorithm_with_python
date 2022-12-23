import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)

start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def get_smallest_node():
    minValue = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < minValue and not visited[i]:
            minValue = distance[i]
            index = i
    return index


def Dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
    
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

Dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])