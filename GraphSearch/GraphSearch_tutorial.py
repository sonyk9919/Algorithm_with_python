from collections import deque

def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
# 8개의 노드를 가진 Graph와 방문한 노드 List
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9

#DFS(graph, 1, visited)
BFS(graph, 1, visited)