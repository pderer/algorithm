from collections import deque
from sys import stdin


input = stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, n + 1):
    graph[i].sort()

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, v, visited):
    visited[v] = True
    q = deque([v])
    while q:
        next = q.popleft()
        print(next, end=" ")
        for neighbor in graph[next]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)

dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)