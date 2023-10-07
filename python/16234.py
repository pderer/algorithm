from collections import deque


n, l, r = map(int, input().split())  # noqa: E741
visited = [[-1] * n for _ in range(n)]

land = [] # 땅
for i in range(n):
    land.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, index):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = index # 연합 표시
    union = land[x][y]
    count = 1
    while queue:
        temp_x, temp_y = queue.popleft()
        for i in range(4):
            nx = temp_x + dx[i]
            ny = temp_y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            temp = abs(land[temp_x][temp_y] - land[nx][ny])
            if temp >= l and temp <= r and visited[nx][ny] == -1:
                visited[nx][ny] = index
                queue.append((nx, ny))
                union += land[nx][ny]
                count += 1
    if count > 1:
        temp = int(union / count)
        for i in range(n):
            for j in range(n):
                if visited[i][j] == index:
                    land[i][j] = temp

count = 0
while True:
    index = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
                bfs(i, j, index)
                index += 1
    if index == n * n:
        break
    visited = [[-1] * n for _ in range(n)] # 초기화 후 다시 bfs
    count += 1

print(count)
