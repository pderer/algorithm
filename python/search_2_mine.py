from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        v = queue.popleft()
        temp_x, temp_y = v[0], v[1]
        if temp_x - 1 >= 0: # 상
            if graph[temp_x - 1][temp_y] == 1:
                queue.append((temp_x - 1, temp_y))
                graph[temp_x - 1][temp_y] = graph[temp_x][temp_y] + 1
        if temp_x + 1 < n: # 하
            if graph[temp_x + 1][temp_y] == 1:
                queue.append((temp_x + 1, temp_y))
                graph[temp_x + 1][temp_y] = graph[temp_x][temp_y] + 1
        if temp_y - 1 >= 0: # 좌
            if graph[temp_x][temp_y - 1] == 1:
                queue.append((temp_x, temp_y - 1))
                graph[temp_x][temp_y - 1] = graph[temp_x][temp_y] + 1
        if temp_y + 1 < m: # 우
            if graph[temp_x][temp_y + 1] == 1:
                queue.append((temp_x, temp_y + 1))
                graph[temp_x][temp_y + 1] = graph[temp_x][temp_y] + 1

bfs(0, 0)
print(graph[n-1][m-1])
        