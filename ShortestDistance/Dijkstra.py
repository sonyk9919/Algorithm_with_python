import sys
input = sys.stdin.readline

INF = 987654321

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for i in range(m):
    #a는 시작점, b는 출발점, c는 cost
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def getMinNode():
    minValue = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] <= minValue and not visited[i]:
            minValue = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
    
    for i in range(n - 1):
        node = getMinNode()
        visited[node] = True
        for j in graph[node]:
            cost = distance[node] + j[1]
            if distance[j[0]] > cost:
                distance[j[0]] = cost

dijkstra(start)
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])