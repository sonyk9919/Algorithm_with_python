from collections import deque

n, m = map(int, input().split(" "))
graph = []

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(int, input())))

def BFS(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[x][y] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    return graph[n - 1][m - 1]

print(BFS(0, 0))
print(graph)

# 105070
# 234567
# 000008
# 14131211109
# 151413121110