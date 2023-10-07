from collections import deque


n, l, r = map(int, input().split())  # noqa: E741
visited = [[0] * n for _ in range(n)]

land = [] # 땅
for i in range(n):
    land.append(list(map(int, input().split())))

# print(visited)
# print(land)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1 # 연합 표시
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
            if temp >= l and temp <= r and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                union += land[nx][ny]
                count += 1
    if count > 1:
        temp = int(union / count)
        print(temp, union, count)
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 1:
                    land[i][j] = temp
        print(land)
    else:
        visited[x][y] = 0 # 연합 실패
        return False

count = 0
while True:
    check = False
    for i in range(n):
        for j in range(n):
            print(i, j)
            bfs(i, j)

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                check = True
                break
    if check is False:
        break
    else:
        visited = [[0] * n for _ in range(n)] # 초기화 후 다시 bfs
        count += 1

print(count)
