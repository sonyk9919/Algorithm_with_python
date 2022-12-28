import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, index = heapq.heappop(q)
        
        if distance[index] < dist:
            continue
        
        for i in graph[index]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

city = 0
time = 0
for i in range(1, n + 1):
    if distance[i] != INF:
        city += 1
        time = max(time, distance[i])

print (city - 1, time)