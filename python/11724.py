import sys


sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, v, visited):
    visited[v] = True
    for neigbor in graph[v]:
        if not visited[neigbor]:
            dfs(graph, neigbor, visited)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1

print(count)